import pandas as pd
import sys
from utils.insert_read_db import read_sql
from utils.json_csv_read import read_json

RAW_JSON_URL = "/home/ninosha/Desktop/archive_task/PSA/raw_data.json"

dw = read_sql()


def count_etl():
    """
    :return: creates file with information of ETL
    """
    data = read_json(open('PSA/raw_data.json', "r", encoding="utf8"))
    data_raw = pd.DataFrame(data)
    number_of_raw_rows = len(data_raw.index)
    size_of_raw = sys.getsizeof(data_raw) / 1024
    dw = read_sql()
    number_of_dw_rows = len(dw.index)
    size_of_dw = sys.getsizeof(dw) / 1024
    incoming_data = f'Incomming Data: {size_of_raw} | {number_of_raw_rows} rows \n'
    dw_data = f'DW Data: {size_of_dw} | {number_of_dw_rows} rows \n'
    data_loss = f'Data Quality: \n {-(100 - (size_of_dw * 100) / size_of_raw)}% of Data lost in ETL'
    f = open("ETL.txt", "w")
    f.write(incoming_data)
    f.write(dw_data)
    f.write(data_loss)
    f.close()



