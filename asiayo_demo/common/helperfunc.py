from rest_framework.response import Response
from rest_framework import status as http_status
from common import errorcode
from common.exceptions import RequestInputParserError
from datetime import datetime, timedelta
import math


def api_response(
    result=None,
    status=http_status.HTTP_200_OK,
    code=errorcode.OK,
    message="success",
    **kargs
):
    content = {}
    if type(result) == dict:
        content.update(result)
    else:
        content["data"] = result

    if "code" not in content:
        content["code"] = code
    if "msg" not in content:
        content["msg"] = message
    return Response(content, status=status, content_type="application/json", **kargs)


def get_request_input(request, method="POST", required_data=[], router={}):
    if method == "GET":
        input_data = dict(request.query_params)
    else:
        input_data = dict(request.data)

    for key in input_data:
        if type(input_data[key]) is list and len(input_data[key]) == 1:
            input_data[key] = input_data[key][0]

    for item in required_data:
        if item not in input_data:
            raise RequestInputParserError("Required data not found: {0}".format(item))

    # Dirty fix
    if request._read_started:
        request._read_started = False
    return input_data, router
