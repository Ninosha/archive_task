import pandas as pd
from sqlalchemy import create_engine


ENGINE = create_engine('postgresql://nino1:qwerty!@localhost:5432/postgres')


def insert_to_db(data_to_insert, table_name):
    """
    :param data_to_insert: requires data you want to insert in database
    :param table_name: table where data must be inserted
    :return:
    """
    data_to_insert.to_sql(table_name, con=ENGINE, if_exists="append", index=False)

    return True


def read_sql():
    res = pd.read_sql('SELECT * FROM iss', ENGINE)

    return res
