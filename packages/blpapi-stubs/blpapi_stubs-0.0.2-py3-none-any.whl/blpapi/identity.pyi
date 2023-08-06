from typing import Any, ClassVar, Union, List

from .chandle import CHandle
from .element import Element
from .service import Service
from .session import Session

class Identity(CHandle):
    INVALID_SEAT: ClassVar[int]
    BPS: ClassVar[int]
    NONBPS: ClassVar[int]
    def __init__(self, handle: Any, sessions: List[Session]) -> None: ...
    def hasEntitlements(
        self, service: Service, entitlements: Union[List[int], Element]
    ) -> bool: ...
    def getFailedEntitlements(
        self, service: Service, entitlements: Union[List[int], Element]
    ) -> tuple[bool, List[int]]: ...
    def isAuthorized(self, service: Service) -> bool: ...
    def getSeatType(self) -> int: ...
