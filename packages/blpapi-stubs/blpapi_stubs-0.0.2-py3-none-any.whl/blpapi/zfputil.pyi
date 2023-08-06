from typing import ClassVar

from .sessionoptions import SessionOptions, TlsOptions

class ZfpUtil:
    REMOTE_8194: ClassVar[int]
    REMOTE_8196: ClassVar[int]
    @staticmethod
    def getZfpOptionsForLeasedLines(
        remote: int, tlsOptions: TlsOptions
    ) -> SessionOptions: ...
