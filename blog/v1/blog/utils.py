import web
import json

def json_response(data):
    web.header("Content-Type", "application/json")
    return json.dumps(data)

def jsondata():
    """Returns the payload, decoded as JSON.
    """
    payload = web.data().decode("utf-8")
    return json.loads(payload)
