import datetime
import json
from typing import Dict
from dataart_python.container import RequestType
import requests

from dataart_python.uploader import Uploader




class Request:
    BASE_URL = "https://src.datartproject.com"

    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_url(self, request_type: RequestType):
        if request_type == RequestType.action:
            return Request.BASE_URL + '/events/send-actions'
        elif request_type == RequestType.identity:
            return Request.BASE_URL + '/users/identify'
        raise ValueError('Request type not correct')

    @classmethod
    def data_builder(cls, event_type, msg):
        date = datetime.datetime.now().astimezone().isoformat()
        if event_type == Uploader.ACTION:
            return json.dumps({
                'timestamp': date,
                'actions': msg
            })
        return msg

    # send event to the
    def post(self, msg, request_type):
        headers = {
            'X-API-Key': self.api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'dataart-python'
        }
        
        url = self.get_url(request_type)
        if request_type == RequestType.action:
            msg = json.loads(msg)
            msg['timestamp'] = datetime.datetime.now().astimezone().isoformat()
            msg = json.dumps(msg)
        response = requests.post(url=url,
                                 data=msg,
                                 headers=headers, )
        return response
