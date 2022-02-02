import pandas as pd
import time


def format_json(raw_json_url):
    """
    :param raw_json_url: gets raw json file url
    :return: formatted dataframe
    """
    while True:
        try:
            # TODO: Error handling
            data = pd.read_json(raw_json_url)

            df = data.drop(labels=['name', 'id'], axis=1)

            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
        except FileNotFoundError as e:
            time.sleep(1)
            continue

        return df


def format_for_db_json(raw_json_url):
    """
    :param raw_json_url: gets raw json file url
    :return: formatted dataframe with last row
    """
    while True:
        try:
            time.sleep(1)
            data = pd.read_json(raw_json_url)
            df = data.drop(labels=['name', 'id'], axis=1)
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
            if df.shape[0] >= 2:
                df = df.drop(df.index[:-1])
            else:
                pass
        except FileNotFoundError as e:
            continue

        return df
