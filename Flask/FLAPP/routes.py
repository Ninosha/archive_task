from Flask.FLAPP import app
from Flask.FLAPP.HELPER_FUNCTIONS.core_functions import get_last_data_quality
from flask_limiter import Limiter, util

limiter = Limiter(app, key_func=util.get_remote_address)


@app.route("/")
def home():
    result = {"message": "go to url: /data_quality"}

    return result


@app.route("/data_quality")
@limiter.limit("100/minute")
def data_quality():
    result = get_last_data_quality()
    res = result.to_html()

    return res
