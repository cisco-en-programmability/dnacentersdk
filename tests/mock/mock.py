import socket
from http.server import HTTPServer
from threading import Thread


from tests.mock.server.v2_3_5_3 import MockServerRequestHandler_v2_3_5_3
from tests.mock.server.v2_3_7_6 import MockServerRequestHandler_v2_3_7_6
from tests.mock.server.v2_3_7_9 import MockServerRequestHandler_v2_3_7_9
from tests.mock.server.v3_1_3_0 import MockServerRequestHandler_v3_1_3_0

HOST = "localhost"


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind((HOST, 0))
    address, port = s.getsockname()
    s.close()
    return port


def get_mock_url(free_port):
    mock_url = "http://{host}:{port}".format(host=HOST, port=free_port)
    return mock_url


def start_mock_server(port, version):
    mockServerHandler = None

    if version == "2.3.5.3":
        mockServerHandler = MockServerRequestHandler_v2_3_5_3
    if version == "2.3.7.6":
        mockServerHandler = MockServerRequestHandler_v2_3_7_6
    if version == "2.3.7.9":
        mockServerHandler = MockServerRequestHandler_v2_3_7_9
    if version == "3.1.3.0":
        mockServerHandler = MockServerRequestHandler_v3_1_3_0

    if mockServerHandler is None:
        raise Exception("Could not create MockServer for version {}".format(version))
    else:
        mock_server = HTTPServer((HOST, port), mockServerHandler)
        mock_server_thread = Thread(target=mock_server.serve_forever)
        mock_server_thread.setDaemon(True)
        mock_server_thread.start()
