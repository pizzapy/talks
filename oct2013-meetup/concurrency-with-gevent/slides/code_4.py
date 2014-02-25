"""
Collecting workers result.
"""

import random
import gevent

def worker(multiplier):
    gevent.sleep(random.random())
    return '*' * multiplier

def producers():
    greenlets = [gevent.spawn(worker, i)
                 for i in range(1, 6)]
    gevent.joinall(greenlets)
    return [g.value for g in greenlets]

print '\n'.join(producers())