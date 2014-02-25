import logging
import short_url


PLEN_BUF_SIZE = 4


def init_logging():
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger('shorty')


def read_bytes(sock, size):
    buf = ''
    while size > 0:
        chunk = sock.recv(size)
        if not chunk:
            raise RuntimeError("unexpected connection close")
        buf += chunk
        size -= len(chunk)
    return buf


def next_id_gen():
    start = 0
    while True:
        start += 1
        yield start
next_id = next_id_gen()


def shorten(long_url):
    # mock saving to db and getting id
    id = next(next_id)
    slug = short_url.encode_url(id)
    return 'http://127.0.0.1:5000/{0}'.format(slug)
