from dataart_python.container import *
from queue import Queue
import json


class Uploader:
    ACTION = 'action'
    IDENTIFY = 'identify'

    def __init__(self, batch_size: int, event_queue: Queue, request_queue: Queue):
        self.batch_size = batch_size
        self.queue_event = event_queue
        self.request_list = request_queue

    def _next_batch(self):
        event_list = [self.queue_event.get(block=True, timeout=25).__dict__ for _ in range(self.batch_size)]
        return event_list

    def upload_action(self, action_con: ActionContainer):
        self.queue_event.put(action_con)

        if self.queue_event.full():
            # get next batch events
            messages = self._next_batch()

            # build request and add to queue
            # print('add to the request list ..........')
            data = json.dumps({
                'timestamp': 'timestamp',
                'actions': messages
            })
            self.request_list.put((RequestType.action, data))
            return True, 'added to queue'

    def upload_identify(self, identify_con: IdentifyContainer):
        json_form = json.dumps(identify_con.__dict__)
        self.request_list.put((RequestType.identity, json_form))
        return True, 'added to request queue'
