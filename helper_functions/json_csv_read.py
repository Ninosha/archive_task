import pandas as pd


def read_json(json_file_path):
    """
    :param json_file_path: json file path
    :return: data from json file
    """

    json_data = pd.read_json(json_file_path)

    return json_data


def read_csv(csv_file_path):
    """
    :param csv_file_path: csv file path
    :return: data from csv file
    """

    csv_data = pd.read_csv(csv_file_path)

    return csv_data
