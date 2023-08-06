import pandas as pd


def iterator2dataframe_complete(iterator):
    """Turn an iterator into multiple small pandas.DataFrame

    This is a balance between memory and efficiency
    """
    chunk_size = 10000
    records = []
    frames = []
    for i, record in enumerate(iterator):
        records.append(record)
        if i % chunk_size == chunk_size - 1:
            frames.append(pd.DataFrame(records))
            records = []
    if records:
        frames.append(pd.DataFrame(records))
    df = pd.concat(frames)
    df = df.astype(str)
    return df


def iterator2dataframe(iterator, chunk_size: int):
    """Turn an iterator into multiple small pandas.DataFrame

    This is a balance between memory and efficiency
    """
    records = []
    for i, record in enumerate(iterator):
        records.append(record)
        if i % chunk_size == chunk_size - 1:
            yield pd.DataFrame(records).astype(str)
            records = []
    if records:
        yield pd.DataFrame(records).astype(str)
