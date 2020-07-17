import socket
from http.server import HTTPServer
from threading import Thread

from tests.mock.server.v1_2_10 import MockServerRequestHandler_v1_2_10
from tests.mock.server.v1_3_0 import MockServerRequestHandler_v1_3_0
from tests.mock.server.v1_3_1 import MockServerRequestHandler_v1_3_1
from tests.mock.server.v1_3_3 import MockServerRequestHandler_v1_3_3
from tests.mock.server.v2_1_1 import MockServerRequestHandler_v2_1_1

HOST = 'localhost'


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind((HOST, 0))
    address, port = s.getsockname()
    s.close()
    return port


def get_mock_url(free_port):
    mock_url = 'http://{host}:{port}'.format(host=HOST, port=free_port)
    return mock_url


def start_mock_server(port, version):
    mockServerHandler = None

    if version == '1.2.10':
        mockServerHandler = MockServerRequestHandler_v1_2_10
    if version == '1.3.0':
        mockServerHandler = MockServerRequestHandler_v1_3_0
    if version == '1.3.1':
        mockServerHandler = MockServerRequestHandler_v1_3_1
    if version == '1.3.3':
        mockServerHandler = MockServerRequestHandler_v1_3_3
    if version == '2.1.1':
        mockServerHandler = MockServerRequestHandler_v2_1_1

    if mockServerHandler is None:
        raise Exception('Could not create MockServer for version {}'.format(version))
    else:
        mock_server = HTTPServer((HOST, port), mockServerHandler)
        mock_server_thread = Thread(target=mock_server.serve_forever)
        mock_server_thread.setDaemon(True)
        mock_server_thread.start()
