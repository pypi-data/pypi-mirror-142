import logging
import signal
import socket
import sys
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from logging.handlers import RotatingFileHandler
from pathlib import Path, PurePath
from typing import Any

import py_eureka_client.eureka_client as EurekaClient  # type: ignore

"""
## Dependencies:
pip install Flask py-eureka-client

## Dev Dependencies:
Install typing stubs.
pip install types-Flask

## pip deploy
<https://packaging.python.org/en/latest/tutorials/packaging-projects/>
cd ~/bin/app/python-service
python3 setup.py sdist
twine upload dist/*
"""


def register_eureka(eureka_server: str, name: str, port: int):
    # get hostname explicitly to avoid ambiguity, e.g, acer vs. acer.lan.
    hostname: str = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("router", 1))
    ip: str = s.getsockname()[0]
    return EurekaClient.init(  # type: ignore
        eureka_server=eureka_server,
        app_name=name,
        instance_port=port,
        instance_host=hostname,
        instance_ip=ip,
    )


def setup_log(log_base: str, name: str) -> logging.Logger:
    flask_logger = logging.getLogger("werkzeug")
    flask_logger.disabled = True

    log_dir = PurePath(log_base, name)
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    log_file = PurePath(log_dir, "service.log")
    log_handler = RotatingFileHandler(
        log_file, mode="a", maxBytes=200 * 1024, backupCount=10, encoding=None
    )
    log_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    log = get_logger()
    log.setLevel(logging.INFO)
    log.addHandler(log_handler)
    return log


def get_logger() -> logging.Logger:
    return logging.getLogger("python_service")


class HttpHandler:
    def set_request_handler(self, request_handler: BaseHTTPRequestHandler):
        self.request_handler = request_handler

    def header(self, content_type: str = "application/json"):
        self.request_handler.send_response(200)
        self.request_handler.send_header("Content-type", content_type)
        self.request_handler.end_headers()

    def body(self, content: str):
        self.request_handler.wfile.write(content.encode("utf-8"))

    def invalid(self):
        self.request_handler.send_response(404)
        self.request_handler.end_headers()

    def path(self):
        return self.request_handler.path

    def get(self):
        self.invalid()

    def post(self):
        self.invalid()


class Handler(BaseHTTPRequestHandler):
    def __init__(self, handler: HttpHandler, *args: Any):
        self.handler = handler
        self.handler.set_request_handler(self)
        BaseHTTPRequestHandler.__init__(self, *args)

    def log_message(self, format, *args):  # type: ignore
        return

    def do_GET(self):
        # Called by Eureka when clicking the instance link on Eureka web UI.
        if self.path == "/info":
            self.handler.header()
            self.handler.body("A Python Service")
        elif self.path == "/health":
            self.handler.header()
            self.handler.body('{"status":"UP"}')
        else:
            self.handler.get()

    def do_POST(self):
        self.handler.post()


class Service:
    def __init__(self, name: str, argparser: ArgumentParser, httpHandler: HttpHandler):
        self.name: str = name
        argparser.add_argument("-log", type=str, required=True, help="base dir for log")
        argparser.add_argument("-port", type=int, required=True, help="service port")
        argparser.add_argument(
            "-eureka", type=str, required=True, help="eureka server url"
        )
        self.args = argparser.parse_args()
        self.port: int = self.args.port
        self.eureka_server: str = self.args.eureka
        self.log: logging.Logger = setup_log(self.args.log, name)
        self.httpHandler = httpHandler

    def start(self):
        eureka_client = register_eureka(self.eureka_server, self.name, self.port)

        def unregister_eureka(signal: Any, frame: Any):
            eureka_client.stop()
            sys.exit(0)

        signal.signal(signal.SIGINT, unregister_eureka)
        signal.signal(signal.SIGTERM, unregister_eureka)

        def handler(*args: Any) -> BaseHTTPRequestHandler:
            return Handler(self.httpHandler, *args)

        httpServer = ThreadingHTTPServer(("", self.port), handler)
        get_logger().info("Serving at " + str(self.port))
        httpServer.serve_forever()
