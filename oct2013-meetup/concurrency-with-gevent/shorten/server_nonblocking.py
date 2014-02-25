import gevent
from gevent import monkey; monkey.patch_socket()
from gevent.pool import Pool
from gevent.socket import socket
import struct
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from common import init_logging, read_bytes, shorten, PLEN_BUF_SIZE

logger = init_logging()

# run server
pool = Pool(100)
server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('', 9000))
server.listen(50)
logger.info('server running...')

def handle(conn, addr):
    """ Handle each connected client. """
    logger.info('connected to {0}'.format(addr))

    gevent.sleep(1)  # delay

    # read payload
    payload_len_buf = read_bytes(conn, PLEN_BUF_SIZE)
    payload_len = struct.unpack('<L', payload_len_buf)[0]
    payload_buf = read_bytes(conn, payload_len)

    # shorten url and send it back
    short_url = shorten(payload_buf)
    payload_len = struct.pack('<L', len(short_url))
    conn.sendall(payload_len + short_url)
    conn.close()

# accept and handle incoming client connections
while True:
    conn, addr = server.accept()
    pool.spawn(handle, conn, addr)
