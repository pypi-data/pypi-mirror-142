from typing import Callable, ClassVar

class Logger:
    SEVERITY_OFF: ClassVar[int]
    SEVERITY_FATAL: ClassVar[int]
    SEVERITY_ERROR: ClassVar[int]
    SEVERITY_WARN: ClassVar[int]
    SEVERITY_INFO: ClassVar[int]
    SEVERITY_DEBUG: ClassVar[int]
    SEVERITY_TRACE: ClassVar[int]
    loggerCallbacksLocal: list
    @staticmethod
    def registerCallback(callback: Callable, thresholdSeverity: int = ...) -> None: ...
    @staticmethod
    def logTestMessage(severity) -> None: ...
