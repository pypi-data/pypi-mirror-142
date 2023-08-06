import sys
from contextlib import closing
from typing import Optional, Union, Iterator

import pandas as pd
import sqlalchemy
from airflow.hooks.jdbc_hook import JdbcHook


class DremioHook(JdbcHook):
    def get_conn(self):
        """
        Get Dremio connection.
        :return: connection
        """
        conn = self.get_connection(getattr(self, self.conn_name_attr))
        host_w_port = conn.host
        login = conn.login
        psw = conn.password
        uri = 'dremio://{}:{}@{}/dremio;SSL=0'.format(login, psw, host_w_port)
        conn = sqlalchemy.create_engine(uri)
        return conn

    def _get_pandas_df_generator(self, sql: str, chunksize: Optional[int] = None) -> Iterator[pd.DataFrame]:
        import pandas.io.sql as psql
        page = 0
        with closing(self.get_conn().connect()) as conn:
            while True:
                if chunksize is not None:
                    offset = page * chunksize
                    sql_ = f'{sql} limit {chunksize} offset {offset}'
                else:
                    sql_ = f'{sql}'
                df = psql.read_sql(sql=sql_, con=conn)
                yield df
                if chunksize is None:
                    break
                if df.shape[0] < chunksize:
                    break
                page += 1

    def get_pandas_df(
            self, sql: str,
            chunksize: Optional[int] = None,
            **kwargs) -> Union[pd.DataFrame, Iterator[pd.DataFrame]]:
        """
        Run query on Dremio instance and return as pandas dataframe.
        :param sql: query to run
        :param chunksize:
        :return:
        """
        if sys.version_info[0] < 3:
            sql = sql.encode('utf-8')
        out = self._get_pandas_df_generator(sql, chunksize)
        if chunksize is None:
            return next(out)
        else:
            return out

    def bulk_dump(self, table, tmp_file):
        super(DremioHook, self).bulk_dump(table, tmp_file)

    def bulk_load(self, table, tmp_file):
        super(DremioHook, self).bulk_load(table, tmp_file)
