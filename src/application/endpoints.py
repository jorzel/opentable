from nameko.web.handlers import http

from werkzeug.wrappers import Request


class HttpService:
    name = "http_service"

    @http("GET", "/up")
    def up(self, request: Request) -> str:
        return "I'm alive"
