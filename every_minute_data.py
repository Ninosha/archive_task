import datetime
import schedule
import time
import pandas as pd
from helper_functions.json_csv_create import create_json
from vars import RAW_JSON_URL

def create_data_every_minute():
    now = datetime.datetime.now()

    def every_minute(func):
        schedule.every(1).minutes.do(func)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def create_file_every_minute():
        time.sleep(1)
        with open(RAW_JSON_URL) as file:
            if file:
                data = pd.read_json(RAW_JSON_URL)
                create_json(data, f"DATA/minute_data/{now.minute}.json")

    every_minute(create_file_every_minute)
    print(f"creating file at minute{now.minute}")


create_data_every_minute()
