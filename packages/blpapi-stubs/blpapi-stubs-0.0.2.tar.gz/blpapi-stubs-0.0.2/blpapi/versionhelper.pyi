from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any

def blpapi_getVersionInfo() -> int: ...
def blpapi_getVersionIdentifier() -> str: ...
