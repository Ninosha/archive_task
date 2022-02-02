def create_json(df, filename):
    """
    :return: creates json file
    """

    df.to_json(filename, orient="records")

    return True


def create_csv(formated_data, filename):
    """
    :return: creates csv file
    """

    formated_data.to_csv(filename, index=False)

    return True
