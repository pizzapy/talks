import uuid
import struct
from socket import socket

from common import init_logging, read_bytes, PLEN_BUF_SIZE

logger = init_logging()

def run():
    # connect to server
    client = socket()
    client.connect(('', 9000))

    # send payload
    payload = 'http://127.0.0.1:5000/{0}'.format(uuid.uuid4())
    payload_len = struct.pack('<L', len(payload))
    client.sendall(payload_len + payload)

    # read payload
    payload_len_buf = read_bytes(client, PLEN_BUF_SIZE)
    payload_len = struct.unpack('<L', payload_len_buf)[0]
    payload_buf = read_bytes(client, payload_len)

    client.close()
    return payload_buf

if __name__ == '__main__':
    print run()
