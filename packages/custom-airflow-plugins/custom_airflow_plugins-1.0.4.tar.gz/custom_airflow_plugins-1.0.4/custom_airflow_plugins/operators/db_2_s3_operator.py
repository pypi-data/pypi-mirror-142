"""
Class for transfer data between some databases to S3 (json or parquet).
"""
from datetime import datetime

import pandas as pd
from airflow.contrib.hooks.mongo_hook import MongoHook
from airflow.exceptions import AirflowException
from airflow.hooks.mysql_hook import MySqlHook
from airflow.hooks.oracle_hook import OracleHook
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

from custom_airflow_plugins.hooks.mssql_hook import MsSqlServerHook
from custom_airflow_plugins.hooks.postgres_hook import PostgreSqlHook
from custom_airflow_plugins.hooks.util import s3


class TransferDB2S3(BaseOperator):
    @apply_defaults
    def __init__(self,
                 source_db: str,
                 source_conn_id: str,
                 dest_s3_conn_id: str,
                 dest_s3_bucket: str,
                 dest_s3_key: str,
                 source_table: str = None,
                 source_query: str = None,
                 source_order_by: str = None,
                 filetype: str = 'parquet',
                 chunksize: int = None,
                 source_mongo_database: str = None,
                 *args, **kwargs):
        super(TransferDB2S3, self).__init__(*args, **kwargs)
        self.source_db = source_db
        self.source_conn_id = source_conn_id
        self.source_table = source_table
        self.source_mongo_database = source_mongo_database
        self.source_query = source_query
        self.source_order_by = source_order_by
        self.dest_s3_conn_id = dest_s3_conn_id
        self.dest_s3_bucket = dest_s3_bucket
        self.dest_s3_key = dest_s3_key
        self.filetype = filetype
        self.chunksize = chunksize

    def execute(self, context):
        if self.source_db.lower() not in ['oracle', 'postgres', 'mssql', 'mysql', 'mongo']:
            raise AirflowException(
                '"source_db" must be one of ["oracle", "postgres", "mssql", "mysql", "mongo"]'
            )

        if self.filetype.lower() not in ['json', 'parquet']:
            raise AirflowException(
                '"filetype" must be one of ["json", "parquet"]'
            )

        if (self.source_table is None) and (self.source_query is None):
            raise AirflowException("source_table or source_query must be defined!")

        if (self.source_table is not None) and (self.source_order_by is None) and (self.source_db != 'mongo'):
            raise AirflowException("source_order_by must be defined when source_table is defined!")

        source = None
        if self.source_db.lower() == 'oracle':
            source = OracleHook(self.source_conn_id)
        elif self.source_db.lower() == 'postgres':
            source = PostgreSqlHook(self.source_conn_id)
        elif self.source_db.lower() == 'mssql':
            source = MsSqlServerHook(self.source_conn_id)
        elif self.source_db.lower() == 'mysql':
            source = MySqlHook(self.source_conn_id)
        elif self.source_db.lower() == 'mongo':
            if self.source_mongo_database is None:
                raise AirflowException("source_mongo_database must be defined!")
            source = MongoHook(self.source_conn_id)

        today = datetime.today().strftime('%Y-%m-%d')

        cleaned = False
        if self.source_db.lower() != 'mongo':
            conn = source.get_conn()
            if (self.source_query is None) and (self.source_table is not None):
                if self.source_order_by is not None:
                    self.source_query = f'select * from {self.source_table} order by {self.source_order_by}'
                else:
                    self.source_query = f'select * from {self.source_table}'

            if self.chunksize:
                chunks = pd.read_sql(self.source_query, con=conn, chunksize=self.chunksize)
                for chunk in chunks:
                    dtime = datetime.now().strftime('%Y%m%d%H%M%S%f')
                    name = f'{self.dest_s3_key}/{today}/file_{dtime}'
                    if not cleaned:
                        s3.clear_s3(s3_conn_id=self.dest_s3_conn_id, bucket=self.dest_s3_bucket, key=self.dest_s3_key)
                        cleaned = True
                    s3.df_2_s3(
                        s3_conn_id=self.dest_s3_conn_id,
                        dataframe=chunk,
                        bucket=self.dest_s3_bucket,
                        key=name,
                        filetype=self.filetype.lower()
                    )
            else:
                df = pd.read_sql(self.source_query, con=conn)
                dtime = datetime.now().strftime('%Y%m%d%H%M%S%f')
                name = f'{self.dest_s3_key}/{today}/file_{dtime}'
                s3.clear_s3(s3_conn_id=self.dest_s3_conn_id, bucket=self.dest_s3_bucket, key=self.dest_s3_key)
                s3.df_2_s3(
                    s3_conn_id=self.dest_s3_conn_id,
                    dataframe=df,
                    bucket=self.dest_s3_bucket,
                    key=name,
                    filetype=self.filetype.lower()
                )
        else:
            # mongo
            from custom_airflow_plugins.util.mongo import iterator2dataframe, iterator2dataframe_complete
            if self.source_table is not None:
                self.source_query = {}
            cursor = source.find(
                mongo_collection=self.source_table,
                query=self.source_query,
                mongo_db=self.source_mongo_database
            )
            if self.chunksize:
                for chunk in iterator2dataframe(iterator=cursor, chunk_size=self.chunksize):
                    dtime = datetime.now().strftime('%Y%m%d%H%M%S%f')
                    name = f'{self.dest_s3_key}/{today}/file_{dtime}'
                    if not cleaned:
                        s3.clear_s3(s3_conn_id=self.dest_s3_conn_id, bucket=self.dest_s3_bucket, key=self.dest_s3_key)
                        cleaned = True
                    s3.df_2_s3(
                        s3_conn_id=self.dest_s3_conn_id,
                        dataframe=chunk,
                        bucket=self.dest_s3_bucket,
                        key=name,
                        filetype=self.filetype.lower(),
                        force_str=True
                    )
            else:
                df = iterator2dataframe_complete(iterator=cursor)
                dtime = datetime.now().strftime('%Y%m%d%H%M%S%f')
                name = f'{self.dest_s3_key}/{today}/file_{dtime}'
                s3.clear_s3(s3_conn_id=self.dest_s3_conn_id, bucket=self.dest_s3_bucket, key=self.dest_s3_key)
                s3.df_2_s3(
                    s3_conn_id=self.dest_s3_conn_id,
                    dataframe=df,
                    bucket=self.dest_s3_bucket,
                    key=name,
                    filetype=self.filetype.lower(),
                    force_str=True
                )




