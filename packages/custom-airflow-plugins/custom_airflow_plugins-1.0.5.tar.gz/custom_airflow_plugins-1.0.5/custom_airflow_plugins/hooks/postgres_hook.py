import numpy as np
import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook
from psycopg2.extensions import register_adapter, AsIs
from typing import Union, Any


# ADAPTERS for compatibility between psycopg2 and pandas
def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)


def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


def addapt_numpy_float32(numpy_float32):
    return AsIs(numpy_float32)


def addapt_numpy_int32(numpy_int32):
    return AsIs(numpy_int32)


def addapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))


register_adapter(np.float64, addapt_numpy_float64)
register_adapter(np.int64, addapt_numpy_int64)
register_adapter(np.float32, addapt_numpy_float32)
register_adapter(np.int32, addapt_numpy_int32)
register_adapter(np.ndarray, addapt_numpy_array)


class PostgreSqlHook(PostgresHook):
    def insert_pandas_df(self,
                         df: Union[pd.DataFrame, Any],
                         table: str,
                         if_exists: str = 'replace',
                         update_data: bool = False,
                         primary_key: str = None,
                         commit_every: int = 5000,
                         schema: str = None):
        """
        Insert a pandas dataframe in database table.
        :param df: Pandas dataframe
        :param table: Postgres table name
        :param if_exists: "replace" or "append", same as dataframe.to_sql argument
        :param update_data: if existing data need to be updated
        :param primary_key: Name of primary key to be created at data table, optional
        :param commit_every: Chunksize, optional
        :param schema: database schema, optional
        :return:
        """
        if df.empty:
            return

        df = df.replace(r'^\s*$', None, regex=True)
        engine = self.get_sqlalchemy_engine()

        if primary_key and update_data and if_exists == 'append':
            # caso a primary key tenha mais de uma chave...
            if ',' in primary_key:
                keys = primary_key.split(',')
                values = []
                command = ''
                for _, data in df.iterrows():
                    command = f"DELETE FROM {table} WHERE "
                    for k in keys:
                        values.append(f"{k}='{data[k]}'")
                with engine.connect() as conn:
                    values_txt = ' AND '.join(values)
                    command = command + values_txt
                    conn.execute(command)
            else:
                excluir_list = ','.join([f"\'{e}\'" for e in df[primary_key].values])
                with engine.connect() as conn:
                    conn.execute(f'DELETE FROM {table} where {primary_key} in ({excluir_list})')

        if primary_key and if_exists == 'replace':
            with engine.connect() as conn:
                conn.execute(f'DROP TABLE IF EXISTS "{table}" CASCADE')

        df.to_sql(
            table,
            con=engine,
            if_exists=if_exists,
            index=False,
            chunksize=commit_every,
            schema=schema
        )

        if primary_key and if_exists == 'replace':
            with engine.connect() as conn:
                conn.execute(f'ALTER TABLE "{table}" ADD PRIMARY KEY ("{primary_key}")')

        engine.dispose()
