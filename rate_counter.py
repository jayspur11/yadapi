import queue
import time


class RateCounter:
    def __init__(self, ttl):
        self._ttl = ttl
        self._values = queue.PriorityQueue()

    def __len__(self):
        self._clean_up()
        return self._values.qsize()

    # Public methods

    def add(self):
        self._values.put(time.time())
        
    def next_event(self):
        try:
            next = self._values.get(block=False)
            self._values.put(next)
            return next + self._ttl - time.time()
        except:
            return 0

    def rate(self):
        return len(self) / self._ttl

    # Private methods

    def _clean_up(self):
        exp = time.time() - self._ttl
        vals = self._values
        while True:
            try:
                earliest = vals.get(block=False)
                if earliest > exp:
                    # still alive, put it back
                    vals.put(earliest)
                    return
            except:
                # everything's gone
                return