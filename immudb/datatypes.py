from dataclasses import dataclass

@dataclass
class SetResponse:
    id: int
    prevAlh: bytes 
    timestamp: int
    eh: bytes
    blTxId: int
    blRoot: bytes
    verified: bool

@dataclass
class SafeGetResponse:
    index: int
    key: bytes
    value: bytes
    timestamp: int
    verified: bool
    refkey: bytes
