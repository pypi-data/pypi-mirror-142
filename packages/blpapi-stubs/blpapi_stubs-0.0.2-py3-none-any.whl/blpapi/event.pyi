from typing import Any, Callable, ClassVar, Optional, List

from .chandle import CHandle
from .message import Message
from .session import Session

class MessageIterator(CHandle):
    def __init__(self, event: Event) -> None: ...
    def __iter__(self) -> MessageIterator: ...
    def __next__(self) -> Message: ...
    next: Callable

class Event(CHandle):
    ADMIN: ClassVar[int]
    SESSION_STATUS: ClassVar[int]
    SUBSCRIPTION_STATUS: ClassVar[int]
    REQUEST_STATUS: ClassVar[int]
    RESPONSE: ClassVar[int]
    PARTIAL_RESPONSE: ClassVar[int]
    SUBSCRIPTION_DATA: ClassVar[int]
    SERVICE_STATUS: ClassVar[int]
    TIMEOUT: ClassVar[int]
    AUTHORIZATION_STATUS: ClassVar[int]
    RESOLUTION_STATUS: ClassVar[int]
    TOPIC_STATUS: ClassVar[int]
    TOKEN_STATUS: ClassVar[int]
    REQUEST: ClassVar[int]
    UNKNOWN: ClassVar[int]
    def __init__(self, handle: Any, sessions: List[Session]) -> None: ...
    def eventType(self) -> int: ...
    def __iter__(self) -> MessageIterator: ...

class EventQueue(CHandle):
    def __init__(self) -> None: ...
    def nextEvent(self, timeout: int = ...) -> Event: ...
    def tryNextEvent(self) -> Optional[Event]: ...
    def purge(self) -> None: ...
