import time
import threading


class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, new_value):
        with self._lock:
            local = self.value
            local += new_value
            time.sleep(0.1)
            self.value = local
