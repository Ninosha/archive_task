import pandas as pd


def format_json(raw_json_url):
    """
    :param raw_json_url: gets raw json file url
    :return: formatted dataframe
    """

    data = pd.read_json(raw_json_url)
    df = pd.DataFrame(data)
    df = df.drop(labels=['name', 'id'], axis=1)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    print(df)
    return df
