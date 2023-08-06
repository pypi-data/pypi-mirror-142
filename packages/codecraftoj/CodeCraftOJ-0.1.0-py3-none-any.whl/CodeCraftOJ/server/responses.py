SUCCESS_NONE = {
    "code": 0,
    "data": None,
    "msg": "Success",
}


def ERROR_UNKNOWN(msg):
    return {
        "code": -1,
        "data": None,
        "msg": msg
    }
