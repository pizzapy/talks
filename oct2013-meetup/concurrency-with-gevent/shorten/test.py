import time
from threading import Thread, Lock
from client import run as run_client

CONCURRENCY = 10

class Runner(object):
    conn_per_sec = 0
    running_agents = 0
    spawned_agents = 0
    lock = Lock()

    def increase_running_agents(self):
        self.lock.acquire()
        self.running_agents += 1
        self.lock.release()

    def decrease_running_agents(self):
        self.lock.acquire()
        self.running_agents -= 1
        self.lock.release()

    def increase_conn_per_sec(self):
        self.lock.acquire()
        self.conn_per_sec += 1
        self.lock.release()

    def reset_conn_per_sec(self):
        self.lock.acquire()
        self.conn_per_sec = 0
        self.lock.release()

    def increase_spawned_agents(self):
        self.lock.acquire()
        self.spawned_agents += 1
        self.lock.release()


class Agent(Thread):
    def __init__(self, runner):
        self.runner = runner
        self.runner.increase_spawned_agents()
        super(Agent, self).__init__()

    def run(self):
        self.runner.increase_running_agents()
        try:
            if run_client():
                self.runner.increase_conn_per_sec()
        except:
            pass
        self.runner.decrease_running_agents()


if __name__ == '__main__':
    runner = Runner()
    start = time.time()

    for _ in range(CONCURRENCY):
        agent = Agent(runner)
        agent.setDaemon(True)
        agent.start()

    print 'spawned {0} agents'.format(runner.spawned_agents)
    while runner.running_agents > 0:
        time.sleep(1)
        print 'connections/second: {0}'.format(runner.conn_per_sec)
        runner.reset_conn_per_sec()

    end = time.time()
    elapsed = end - start
    print 'took: {0}'.format(elapsed)
