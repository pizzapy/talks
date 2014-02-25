"""
Synchronous.
"""

import time
import random

def worker(multiplier):
    time.sleep(random.random())
    print '*' * multiplier

for i in range(1, 6):
    worker(i)