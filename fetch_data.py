import requests as rq


def fetch_data():
    """
    :param url: URL from where to fetch data
    :return: requested data in json
    """

    api_response = rq.get("https://api.wheretheiss.at/v1/satellites/25544")

    requested_data = api_response.json()

    return requested_data

