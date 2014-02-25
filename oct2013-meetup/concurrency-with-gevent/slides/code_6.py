"""
Limit concurrent workers using pool.
"""

import random
import gevent
from gevent.queue import Queue
from gevent.pool import Pool

pool = Pool(2)
tasks = Queue()

def worker(multiplier):
    gevent.sleep(random.random())
    tasks.put('*' * multiplier)

def producers():
    pool.map(worker, range(1, 6))

def consumer():
    while True:
        print tasks.get()

gevent.spawn(consumer)
producers()
