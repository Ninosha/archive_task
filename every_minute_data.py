import datetime
import schedule
import time
import pandas as pd
from utils.json_csv_create import create_json


def create_data_every_minute():
    now = datetime.datetime.now()

    def every_minute(func):
        schedule.every(5).second.do(func)
        while True:
            schedule.run_pending()
            time.sleep(1)

        # from time import time, sleep
        # while True:
        #     sleep(60 - time() % 60)
        #     func()

    def create_file_every_minute():
        with open("PSA/raw_data.json", "r") as file:
            if file:
                data = pd.read_json("PSA/raw_data.json")
                df = pd.DataFrame(data)
                df.to_json(f"{now.minute}.json", orient="records")
                create_json(df, now.minute)
            else:
                print("sh")

    return every_minute(create_file_every_minute)
