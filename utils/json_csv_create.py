
def create_json(df, filename):
    """
    :return: creats json file
    """

    df.to_json(f"{filename}.json", orient="records")

    return True


def create_csv(formated_data ,filename):
    """
    :return: creats csv file
    """

    formated_data.to_csv(f"{filename}.csv" ,index=False)

    return True
