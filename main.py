from helper_functions.json_csv_create import create_json, create_csv
from helper_functions.format_json import format_json
from transform_mart import insert_mart_to_db
from fetch_data import fetch_data
from vars import RAW_JSON_URL

# CHECKED
fetched_data = fetch_data()

# CHECKED
formatted = format_json(raw_json_url=RAW_JSON_URL)

# CHECKED
insert_mart_to_db(RAW_JSON_URL)


# TODO: Filename
create_json(formatted, "DATA/formatted_json/satelite.json")

# TODO: Filename
create_csv(formatted, "DATA/formatted_csv/satelite.csv")

