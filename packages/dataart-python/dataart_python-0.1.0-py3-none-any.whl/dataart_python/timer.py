import time


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        elapsed_time = time.perf_counter() - self.start_time
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
