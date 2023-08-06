import queue
import threading
from dataart_python.request import Request


class Worker(threading.Thread):
    def __init__(self, requests: queue.Queue, api_key: str, id: str):
        threading.Thread.__init__(self)
        self.request_queue = requests
        self.id = id
        self.api_key = api_key
        self.running = True

    def upload(self):
        req = Request(api_key=self.api_key)
        if not self.request_queue.empty():
            try:
                request_type, messages = self.request_queue.get(block=True, timeout=20)
                response = req.post(messages, request_type)
                print('thread id {} done - > {} event type : {}'.format(self.id, response.status_code,
                                                                        request_type))
            except Exception:
                print('exception in sending request')

    def run(self) -> None:
        while self.running:
            self.upload()

    def enqueue(self, item):
        self.request_queue.put(item)

    def shutdown(self):
        self.running = False
