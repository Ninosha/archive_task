import datetime
from helper_functions.insert_read_db import read_sql
from helper_functions.json_csv_read import read_json
from vars import ENGINE
import time
from vars import RAW_JSON_URL


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return round(((current - previous) / previous) * 100.0, 2)
    except ZeroDivisionError:
        return float('inf')


def create_data_quality():
    """
    :return: creates file with data quality info
    """

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = read_json(RAW_JSON_URL)
    memory_raw_in_mb = data.memory_usage(deep=True).sum() / 1024
    number_of_raw_data_rows = data.shape[0]

    dw = read_sql(ENGINE)
    memory_dw_in_mb = dw.memory_usage(deep=True).sum() / 1024
    number_of_dw_rows = dw.shape[0]
    SQL = """INSERT INTO iss_data_quality("timestamp", incoming_mb, incoming_raw, dw_mb, memory_dw, 
    raws_quality_percentage, memory_quality_percentage) VALUES (%s, %s, %s, %s, %s, %s, %s); """

    percentage_change_of_rows = get_change(number_of_raw_data_rows, number_of_dw_rows)
    percentage_change_of_memory = get_change(memory_raw_in_mb, memory_dw_in_mb)
    ENGINE.execute(SQL, (
        now, memory_raw_in_mb, number_of_raw_data_rows, memory_dw_in_mb, number_of_dw_rows, percentage_change_of_rows,
        percentage_change_of_memory))

    x = [now, memory_raw_in_mb, number_of_raw_data_rows, memory_dw_in_mb, number_of_dw_rows, percentage_change_of_rows,
         percentage_change_of_memory]
    print(x)


while 1:
    try:
        create_data_quality()
    except Exception as ee:
        continue
    time.sleep(1)
