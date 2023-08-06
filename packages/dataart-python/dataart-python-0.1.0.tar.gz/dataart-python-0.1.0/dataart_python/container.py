from datetime import datetime
from typing import Dict
from enum import Enum



class ActionContainer:
    def __init__(self, event_key: str, user_key: str, is_anonymous: bool, metadata: Dict, timestamp: datetime):
        self.key = event_key
        self.user_key = user_key
        self.is_anonymous_user = is_anonymous
        self.metadata = metadata
        self.timestamp = timestamp.astimezone().isoformat()


class IdentifyContainer:
    def __init__(self, user_key: str, metadata: Dict):
        self.user_key = user_key
        self.metadata = metadata

class RequestType(Enum):
    action = 'action'
    identity = 'identity'