import pandas as pd
from helper_functions.format_json import format_for_db_json
from sqlalchemy import create_engine

RAW_JSON_URL = "/home/ninosha/Desktop/archive_task/DATA/PSA/raw_data.json"


def insert_to_db(data_to_insert, table_name, engine):
    """
    :param engine: sqlalchemy engine
    :param data_to_insert: requires data you want to insert in database
    :param table_name: table where data must be inserted
    :return:
    """
    data_to_insert.to_sql(table_name, con=engine, if_exists="append", index=False)
    return True


def insert_formatted_into_db():
    """
    :return: inserts last row of formatted data into db
    """
    try:
        ENGINE = create_engine('postgresql://nino1:qwerty!@localhost:5432/postgres')
        formatted = format_for_db_json(RAW_JSON_URL)
        insert_to_db(formatted, "iss", ENGINE)
        print(f"{formatted} inserting to db")
    except Exception as e:
        raise ConnectionError(f"{e}")


def read_sql(engine):
    """
    :param engine: sqlalchemy engine
    :return: data from database
    """
    res = pd.read_sql("SELECT * FROM iss", engine)

    return res
