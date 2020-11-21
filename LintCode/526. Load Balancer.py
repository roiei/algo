import random


class LoadBalancer:
    def __init__(self):
        self.servers = []
        self.n = 0

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id not in self.servers:
            self.servers += server_id,
            self.n += 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id in self.servers:
            self.servers.remove(server_id)
            self.n -= 1

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        if self.n > 0:
            idx = random.randint(0, self.n - 1)
            return self.servers[idx]
        return None


stime = time.time()
lb = LoadBalancer()
lb.add(1)
lb.add(2)
lb.add(3)
lb.pick()
lb.pick()
lb.pick()
lb.pick()
lb.remove(1)
lb.pick()
lb.pick()
lb.pick()
print('elapse time: {} sec'.format(time.time() - stime))