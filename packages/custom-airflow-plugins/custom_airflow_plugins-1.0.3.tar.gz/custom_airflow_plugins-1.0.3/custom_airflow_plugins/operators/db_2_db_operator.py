"""
Class for transfer data between some databases to another database.
"""

from airflow.exceptions import AirflowException
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

from custom_airflow_plugins.hooks.dremio_hook import DremioHook
from custom_airflow_plugins.hooks.mssql_hook import MsSqlServerHook
from custom_airflow_plugins.hooks.postgres_hook import PostgreSqlHook


class TransferDB2DB(BaseOperator):
    @apply_defaults
    def __init__(self,
                 source_db: str,
                 source_conn_id: str,
                 dest_db: str,
                 dest_conn_id: str,
                 dest_table: str,
                 dest_schema: str = None,
                 source_table: str = None,
                 source_query: str = None,
                 source_order_by: str = None,
                 commit_every: int = 1000,
                 if_exists: str = 'replace',
                 *args, **kwargs):
        super(TransferDB2DB, self).__init__(*args, **kwargs)
        self.source_db = source_db
        self.source_conn_id = source_conn_id
        self.source_table = source_table
        self.source_query = source_query
        self.source_order_by = source_order_by
        self.commit_every = commit_every
        self.dest_db = dest_db
        self.dest_conn_id = dest_conn_id
        self.dest_table = dest_table
        self.dest_schema = dest_schema
        self.if_exists = if_exists

    def execute(self, context):
        if (self.source_table is None) and (self.source_query is None):
            raise AirflowException("source_table or source_query must be defined!")

        if (self.source_table is not None) and (self.source_order_by is None):
            raise AirflowException("source_order_by must be defined when source_table is defined!")

        if self.source_db.lower() not in ['postgres', 'mssql', 'oracle', 'dremio']:
            raise AirflowException(
                '"source_db" must be one of ["postgres", "mssql", "oracle", "dremio"]'
            )

        if self.dest_db.lower() not in ['postgres', 'mssql']:
            raise AirflowException(
                '"dest_db" must be one of ["postgres", "mssql"]'
            )

        if self.if_exists.lower() not in ['replace', 'append']:
            raise AirflowException(
                '"if_exists" must be one of ["replace", "append"]'
            )

        source = None
        if self.source_db.lower() == 'postgres':
            source = PostgreSqlHook(self.source_conn_id)
        elif self.source_db.lower() == 'mssql':
            source = MsSqlServerHook(self.source_conn_id)
        elif self.source_db.lower() == 'dremio':
            source = DremioHook(self.source_conn_id)

        dest = None
        if self.dest_db.lower() == 'postgres':
            dest = PostgreSqlHook(self.dest_conn_id)
        elif self.dest_db.lower() == 'mssql':
            dest = MsSqlServerHook(self.dest_conn_id)

        # reading table
        if self.source_table is not None:
            if self.source_order_by is not None:
                self.source_query = f'select * from {self.source_table} order by {self.source_order_by}'
            else:
                self.source_query = f'select * from {self.source_table}'
        for chunk in source.get_pandas_df(sql=self.source_query, chunksize=self.commit_every):
            # saves into dest db
            dest.insert_pandas_df(
                df=chunk,
                table=self.dest_table,
                if_exists=self.if_exists,
                commit_every=self.commit_every,
                schema=self.dest_schema
            )
            self.if_exists = 'append'
