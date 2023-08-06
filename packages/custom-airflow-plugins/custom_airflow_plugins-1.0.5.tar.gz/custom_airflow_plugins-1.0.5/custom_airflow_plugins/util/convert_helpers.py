import pandas as pd
import datetime
from typing import List, Optional


def date_to_mongo(dictlist: List) -> List:
    for d in dictlist:
        for k, v in d.items():
            print(type(v))
            if type(v) == datetime.date:
                try:
                    v = pd.Timestamp(datetime.datetime.strftime(v, '%Y-%m-%d %H:%M:%S'))
                except:
                    v = None
                d.update({k: v})
    return dictlist


def df_convert_columns_str(dataframe: pd.DataFrame, except_cols: Optional[List]) -> pd.DataFrame:
    columns = [c for c in dataframe.columns if c not in except_cols]
    for c in columns:
        dataframe[c] = dataframe[c].astype(str)
    return dataframe
