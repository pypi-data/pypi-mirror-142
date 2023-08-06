import atexit
import queue
from typing import Dict
from datetime import datetime
from dataart_python.uploader import Uploader
from dataart_python.container import ActionContainer, IdentifyContainer
from dataart_python.worker import Worker


def validate_config(api_key, worker_nums, batch_size):
    if len(api_key) < 1:
        raise ValueError('api_key can\'t  be empty')
    if worker_nums == 0:
        raise ValueError('worker_nums can\'t be less than 1')
    if batch_size == 0:
        raise ValueError('batch_size can\'t be less than 1')
    return None


# use for creating new client for using in the classes
class DataArt:

    def __init__(self, api_key: str, worker_nums: int = 4, batch_size: int = 10):
        if validate_config(api_key, worker_nums, batch_size) is None:
            self.events_queue = queue.Queue(maxsize=batch_size)
            self.requests_queue = queue.Queue()
            self.uploader = Uploader(batch_size, self.events_queue, self.requests_queue)
            self.workers = []
            self.worker_nums = worker_nums
            self.api_key = api_key
            # create some workers

    def stop_workers(self):
        pass

    def start(self):
        for i in range(self.worker_nums):
            manager = Worker(self.requests_queue, api_key=self.api_key, id=str(i))
            self.workers.append(manager)
            manager.start()
        atexit.register(self.shutdown)

    def emit_action(self,
                    user_key: str,
                    event_key: str,
                    metadata: Dict,
                    timestamp: datetime,
                    is_anonymous_user: bool = False):
        return self.uploader.upload_action(
            ActionContainer(event_key=event_key,
                            user_key=user_key,
                            is_anonymous=is_anonymous_user,
                            timestamp=timestamp,
                            metadata=metadata))

    def identify(self,
                 user_key: str,
                 metadata: Dict):
        return self.uploader.upload_identify(
            IdentifyContainer(user_key=user_key,
                              metadata=metadata))

    def flush(self):
        self.events_queue.join()
        self.requests_queue.join()
        pass

    def shutdown(self):
        worker: Worker
        for worker in self.workers:
            worker.shutdown()
        try:
            worker.join()  # TODO solve warning
        except RuntimeError:
            print('RuntimeError occurred will joining workers')


# create new client or return error
def new_client(config: Dict):
    pass
