import enum
from typing import Tuple, List, Type
from pydantic import BaseModel



class MessageType(enum.Enum):
    PLAYER_DEATH = 1
    PLAYER_CHAT = 2
    PLAYER_ADVANCEMENT = 3
    QQ_GROUP = 4 # Deprecated
    PLAYER_LIST_REQUEST = 5
    PLAYER_LIST_RESPONSE = 6
    SERVER_PING = 7
    SERVER_PONG = 8
    PLAYER_JOIN = 9
    PLAYER_LEAVE = 10



class Message(BaseModel):
    client_name: str
    client_id: int
    msg_type: MessageType
    content: str

class PlayerListResponseMessage(Message):
    online_players: List[str]


class PlayerMessage(Message):
    player_name: str


class PlayerDeathMessage(PlayerMessage):
    index: int
    death_position: Tuple[float, float, float]
    death_dim: int  # Dim ID


class PlayerAdvancementMessage(PlayerMessage):
    pass


class PlayerChatMessage(PlayerMessage):
    pass



MessageRegistry = {
    MessageType.PLAYER_ADVANCEMENT: PlayerAdvancementMessage,
    MessageType.PLAYER_CHAT: PlayerChatMessage,
    MessageType.PLAYER_DEATH: PlayerDeathMessage,
    MessageType.PLAYER_LIST_RESPONSE: PlayerListResponseMessage,
    MessageType.PLAYER_JOIN: PlayerMessage,
    MessageType.PLAYER_LEAVE: PlayerMessage,
}

def get_class(t: MessageType) -> Type[Message]:
    try:
        return MessageRegistry[t]
    except KeyError:
        return Message
