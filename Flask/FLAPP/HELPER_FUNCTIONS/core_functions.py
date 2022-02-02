import pandas as pd
from sqlalchemy import create_engine

# from vars import ENGINE
ENGINE = create_engine('postgresql://nino1:qwerty!@localhost:5432/postgres')


def get_last_data_quality():
    """
    :return: opens connection with db and closes when function is over. returns last minute data from data_quality table
    """
    last_second_data = pd.read_sql('select "timestamp", incoming_mb, incoming_raw, dw_mb, memory_dw, '
                                   'raws_quality_percentage,memory_quality_percentage '
                                   'from iss_data_quality ORDER BY timestamp DESC LIMIT 1', con=ENGINE)
    return last_second_data






