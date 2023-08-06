from collections.abc import Mapping as Mapping_t
import datetime as dt
from typing import Any, Union, Optional

from .chandle import CHandle
from .element import Element
from .event import Event
from .internals import CorrelationId
from .name import Name
from .topic import Topic

class EventFormatter(CHandle):
    latestMessageName: Any
    def __init__(self, event: Event) -> None: ...
    def appendMessage(
        self,
        messageType: Union[Name, str],
        topic: Topic,
        sequenceNumber: Optional[int] = ...,
    ) -> None: ...
    def appendResponse(self, operationName: Union[Name, str]) -> None: ...
    def appendRecapMessage(
        self,
        topic: Topic,
        correlationId: Optional[CorrelationId] = ...,
        sequenceNumber: Optional[int] = ...,
        fragmentType: int = ...,
    ) -> None: ...
    def setElement(
        self,
        name: Union[Name, str],
        value: Union[bool, str, int, float, dt.datetime, Name],
    ) -> None: ...
    def setElementNull(self, name: Union[Name, str]) -> None: ...
    def pushElement(self, name: Union[Name, str]) -> None: ...
    def popElement(self) -> None: ...
    def appendValue(
        self, value: Union[bool, str, int, float, dt.datetime, Name]
    ) -> None: ...
    def appendElement(self) -> None: ...
    def fromPy(
        self,
        value: Mapping_t[
            Union[Name, str], Union[Element, bool, str, dt.datetime, int, float, Name]
        ],
    ) -> None: ...
