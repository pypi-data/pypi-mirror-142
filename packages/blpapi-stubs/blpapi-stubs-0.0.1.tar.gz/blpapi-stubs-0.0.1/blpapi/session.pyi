from typing import Callable, ClassVar, Optional

from .abstractsession import AbstractSession
from .event import Event, EventQueue
from .identity import Identity
from .internals import CorrelationId
from .request import Request
from .requesttemplate import RequestTemplate
from .service import Service
from .sessionoptions import SessionOptions
from .subscriptionlist import SubscriptionList

class Session(AbstractSession):
    UNSUBSCRIBED: ClassVar[int]
    SUBSCRIBING: ClassVar[int]
    SUBSCRIBED: ClassVar[int]
    CANCELLED: ClassVar[int]
    PENDING_CANCELLATION: ClassVar[int]
    def __init__(
        self,
        options: Optional[SessionOptions] = ...,
        eventHandler: Optional[Callable[[Event, "Session"], Optional[bool]]] = ...,
        eventDispatcher: Optional[Callable[[Event, "Session"], Optional[bool]]] = ...,
    ) -> None: ...
    def start(self) -> bool: ...
    def startAsync(self) -> bool: ...
    def stop(self) -> bool: ...
    def stopAsync(self) -> bool: ...
    def nextEvent(self, timeout: Optional[int] = ...) -> Event: ...
    def tryNextEvent(self) -> Optional[Event]: ...
    def subscribe(
        self,
        subscriptionList: SubscriptionList,
        identity: Optional[Identity] = ...,
        requestLabel: Optional[str] = ...,
    ) -> None: ...
    def unsubscribe(self, subscriptionList: SubscriptionList) -> None: ...
    def resubscribe(
        self,
        subscriptionList: SubscriptionList,
        requestLabel: Optional[str] = ...,
        resubscriptionId: Optional[int] = ...,
    ) -> None: ...
    def setStatusCorrelationId(
        self,
        service: Service,
        correlationId: CorrelationId,
        identity: Optional[Identity] = ...,
    ) -> None: ...
    def sendRequest(
        self,
        request: Request,
        identity: Optional[Identity] = ...,
        correlationId: Optional[CorrelationId] = ...,
        eventQueue: Optional[EventQueue] = ...,
        requestLabel: Optional[str] = ...,
    ) -> Optional[CorrelationId]: ...
    def sendRequestTemplate(
        self,
        requestTemplate: RequestTemplate,
        correlationId: Optional[CorrelationId] = ...,
    ) -> Optional[CorrelationId]: ...
    def createSnapshotRequestTemplate(
        self,
        subscriptionString: str,
        correlationId: CorrelationId,
        identity: Optional[Identity] = ...,
    ) -> RequestTemplate: ...
