import schedule
import pandas as pd
from fetch_data import fetch_data
from utils.json_csv_read import read_json
import time
import sys


fetched_data = [fetch_data()]
df = pd.DataFrame(fetched_data)


def create_raw_data(fetched_raw_data):
    """
    :return: creates raw data json in PSA directory
    """

    df.to_json("PSA/raw_data.json", orient="records")

    def per_second(func):
        """
        :param func: function to repeat every second
        :return: creates function every second
        """
        schedule.every(1).second.do(func)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def append_to_raw_json():
        """
        :return: joins present raw data with old raw data in pandas dataframe and creates raw_danewta
        """
        df = pd.DataFrame([fetched_raw_data])
        df.reset_index(drop=True)
        data = read_json(open('PSA/raw_data.json', "r", encoding="utf8"))
        df1 = pd.DataFrame(data)
        df1.reset_index(drop=True)
        df3 = df1.append(df)
        df3.reset_index(drop=True)
        df3.to_json('PSA/raw_data.json', orient="records")

    # per_second(append_to_raw_json)


