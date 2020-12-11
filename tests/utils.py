from json import dumps
from unittest.mock import MagicMock

from werkzeug.datastructures import MultiDict
from werkzeug.wrappers import Request


class RequestFactory:
    def __call__(self, method="GET", form=None, json=None, args=None):
        request = MagicMock(spec=Request)
        request.method = method
        request.args = {} if args is None else args
        request.headers = {}
        if form is not None:
            request.mimetype = "application/form-data"
            request.form = MultiDict(form)
        elif json is not None:
            request.mimetype = "application/json"
            request.data = dumps(json).encode("utf-8")
        request.get_data = MagicMock(return_value=request.data)
        return request
