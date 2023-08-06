from .message import *
from typing import Any, Callable, Dict
class Dispatcher:

    def __init__(self) -> None:
        self.message_listener = {}
    
    def add_message_listener(self, msg_type: MessageType, func: Callable):
        try:
            self.message_listener[msg_type.value].append(func)
        except KeyError:
            self.message_listener[msg_type.value] = []
            self.message_listener[msg_type.value].append(func)

    def feed_packet(self, packet: bytes):
        msg_json = str(packet, encoding='UTF-8')
        # parse msg to obj here
        msg = Message.parse_raw(msg_json)
        msg_cls = get_class(msg.msg_type)
        msg = msg_cls.parse_raw(msg_json) # Shadowing msg
        try:
            for f in self.message_listener[msg.msg_type.value]:
                f(msg)
        except KeyError:
            pass
    
    def on(self, msg_type: MessageType) -> Callable:
        def decorator(func: Callable) -> Callable[[Message], Any]:
            self.add_message_listener(msg_type, func)
            return func
        return decorator


