"""
1. latitude/longitude  - The combination of these two components specifies the position of any location on the surface
of Earth. timestamp
2. Altitude or elevation pinpoints the height above a reference point, usually sea level.  time stamp
3. footprint - It is the area of the earth visible to the satellite. time stamp
4. solar lat and solar lon  timestamp
5. visibility time stamp footprint
6.latitude longitude velocity timestamp - determine the trajectory of the orbiting body in space.
"""
from format_json import format_json
from utils.insert_read_db import insert_to_db
import pandas as pd


RAW_JSON_URL = "/home/ninosha/Desktop/archive_task/PSA/raw_data.json"


def insert_mart_to_db():
    """
    :return: inserts mart to db
    """
    def create_mart(list_of_columns):
        """
        :param list_of_columns: list of columns needed
        :return: returns mart
        """
        formated_json = format_json(raw_json_url=RAW_JSON_URL)

        df = pd.DataFrame(formated_json)
        mart = df.filter(items=list_of_columns)
        return mart

    def insert_db():
        """
        :return: inserts mart to db
        """
        position = create_mart(['latitude', 'longitude', "timestamp"])
        distance = create_mart(['velocity', "timestamp"])
        height = create_mart(['altitude', "timestamp"])
        footprint = create_mart(['footprint', "timestamp"])
        visibility = create_mart(['visibility', 'timestamp'])
        trajectory = create_mart(['latitude', 'longitude', "velocity", "timestamp"])

        insert_to_db(position, "satelite_position")
        insert_to_db(distance, "satelite_distance")
        insert_to_db(height, "satelite_height")
        insert_to_db(footprint, "satelite_footprint")
        insert_to_db(visibility, "satelite_visibility")
        insert_to_db(trajectory, "satelite_trajectory")

    insert_db()

    return True