"""
Workers results on queue consumed by consumer.
"""

import random
import gevent
from gevent.queue import Queue

tasks = Queue()

def worker(multiplier):
    gevent.sleep(random.random())
    tasks.put('*' * multiplier)

def producers():
    greenlets = [gevent.spawn(worker, i) for i in range(1, 6)]
    gevent.joinall(greenlets)

def consumer():
    while True:
        print tasks.get()

gevent.spawn(consumer)
producers()
