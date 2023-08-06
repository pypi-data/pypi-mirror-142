import logging, msgpack
from uuid import UUID, uuid4
from datetime import datetime
from typing import NamedTuple, Any, Union
from asyncio import Event
from websockets.legacy.protocol import WebSocketCommonProtocol 

logger = logging.getLogger(__package__)

def _decoder(obj: Any) -> Any:
    if b'__datetime__' in obj:
        obj = datetime.strptime(obj[b'as_str'].decode(), "%Y-%m-%dT%H:%M:%S.%f")
    elif b'__datetimetz__' in obj:
        obj = datetime.strptime(obj[b'as_str'].decode(), "%Y-%m-%dT%H:%M:%S.%f%z")
    return obj

def _encoder(obj: Any) -> Any:
    if isinstance(obj, datetime):
        if obj.tzinfo is None:
            obj = {b'__datetime__': True, b'as_str': obj.strftime("%Y-%m-%dT%H:%M:%S.%f").encode()}
        else:
            obj = {b'__datetimetz__': True, b'as_str': obj.strftime("%Y-%m-%dT%H:%M:%S.%f%z").encode()}
    return obj

def packb(obj: Any) -> Union[bytes, None]:
    return msgpack.packb(obj, default=_encoder)

def unpackb(obj: bytes) -> Union[Any, None]:
    return msgpack.unpackb(obj, object_hook=_decoder)

class Message(NamedTuple):
    uid: bytes
    reference: bytes
    channel: str
    subject: str
    data: any
    def __repr__(self):
        elements = [
            UUID(bytes=self.uid).hex,
            UUID(bytes=self.reference).hex if self.reference else None,
            self.channel,
            self.subject
        ]
        return f"<Message({', '.join([str(e) for e in elements])})>"

class Connection(object):

    def __init__(self, ws: WebSocketCommonProtocol, debug=False):
        self._debug = debug
        self._ws = ws
        logging.debug(f"Creating connection {self.id}")
        self._ack = Event()
        self._ack.set()
        # self._unacked: list[bytes] = []

    def __repr__(self):
        return f"<Connection {self.id.hex}>"

    @property
    def id(self) -> UUID:
        return self._ws.id

    async def send(self, msg: Message):
        logging.debug(f"{self.id.hex[20:]} -> {msg}")
        await self._ws.send(packb(msg))
        await self._ack.wait()

    async def recv(self) -> Message:
        while True:
            msg = Message(*unpackb(await self._ws.recv()))
            logging.debug(f"{self.id.hex[20:]} <- {msg}")
            if msg.channel == 'system' and msg.subject == 'ack':
                self._ack.set()
                continue
            else:
                await self._ws.send(packb(Message(uuid4().bytes, msg.uid, 'system', 'ack', None)))
            return msg

    async def close(self):
        logging.debug(f"Closing connection {self.id.hex}")
        # self._unacked = []
        # self._CTS.set()
        self._ack.set()
        if not self._ws.closed:
            await self._ws.close()

