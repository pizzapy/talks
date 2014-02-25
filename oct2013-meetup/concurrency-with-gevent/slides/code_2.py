"""
Basic workers printing.
"""

import gevent
import random

def worker(multiplier):
    gevent.sleep(random.random())
    print '*' * multiplier

greenlets = [gevent.spawn(worker, i)
             for i in range(1, 6)]
gevent.joinall(greenlets)