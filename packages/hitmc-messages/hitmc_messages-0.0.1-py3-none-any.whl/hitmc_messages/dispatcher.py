from .message import *
from typing import Any, Callable, Dict
class Dispatcher:

    message_listener: Dict[int, List[Callable[[Message], Any]]] = {}

    @classmethod
    def add_message_listener(cls, msg_type: MessageType, func: Callable[[Message], Any]):
        try:
            cls.message_listener[msg_type.value].append(func)
        except KeyError:
            cls.message_listener[msg_type.value] = []
            cls.message_listener[msg_type.value].append(func)

    @classmethod
    def feed_packet(cls, packet: bytes):
        msg_json = str(packet, encoding='UTF-8')
        # parse msg to obj here
        msg = Message.parse_raw(msg_json)
        msg_cls = get_class(msg.msg_type)
        msg = msg_cls.parse_raw(msg_json) # Shadowing msg
        try:
            for f in cls.message_listener[msg.msg_type.value]:
                f(msg)
        except KeyError:
            pass
    
    @classmethod
    def on(cls, msg_type: MessageType) -> Callable:
        def decorator(func: Callable) -> Callable[[Message], Any]:
            cls.add_message_listener(msg_type, func)
            return func
        return decorator


