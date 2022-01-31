from utils.json_csv_create import create_json, create_csv
from create_raw_data import create_raw_data
from utils.insert_read_db import insert_to_db
from format_json import format_json
from every_minute_data import create_data_every_minute
from transform_mart import insert_mart_to_db
from fetch_data import fetch_data
from count_etl import count_etl

"""
1. request data: every second
2. create json with raw data
3. cron(min): creat files once in minute
4. read.json
5. transform json
6. transform for mart
7. create mart
8. insert transformed json to db
9. insert transformed mart json to db with diff tables
10.create json and csv from transformed json(1)
"""

RAW_JSON_URL = "/home/ninosha/Desktop/archive_task/PSA/raw_data.json"
# fetched_data = fetch_data()
#
# # request data: every second and save into raw data
# create_raw_data(fetched_raw_data=fetched_data)

# cron(min): creat files once in minute
# create_data_every_minute()

# transform json
formated_json = format_json(raw_json_url=RAW_JSON_URL)
# transform for mart and add to db
insert_mart_to_db()

# insert transformed mart json to db with diff tables
insert_to_db(formated_json, "iss")

# create json and csv from transformed json
create_json(formated_json, "formated_json/satelite")

create_csv(formated_json, "formated_csv/satelite")

# count data ETL
count_etl()
