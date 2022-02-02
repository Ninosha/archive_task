from helper_functions.insert_read_db import insert_formatted_into_db
from helper_functions.create_per_second import per_second
import time

while True:
    try:
        insert_formatted_into_db()
    except ValueError as e:
        continue
    time.sleep(1)
