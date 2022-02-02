import schedule


def per_second(func):
    """
    :param func: function to repeat every second
    :return: creates function every second
    """
    schedule.every(1).second.do(func)
    while True:
        schedule.run_pending()
