import pytest

from immu import item

emptyLeaf = bytes([
    0xa, 0x88, 0x11, 0x18, 0x52, 0x9, 0x5c, 0xae, 0x4, 0x53, 0x40, 0xea, 0x1f, 0xb, 0x27, 0x99, 0x44, 0xb2, 0xa7, 0x56, 0xa2, 0x13, 0xd9, 0xb5, 0x1, 0x7, 0xd7, 0x48, 0x97, 0x71, 0xe1, 0x59
])

testLeaf = bytes([
    0x62, 0x2e, 0x82, 0xa6, 0x42, 0x48, 0x2c, 0x58, 0x96, 0x92, 0x3, 0xba, 0xda, 0x74, 0x40, 0x97, 0xc9, 0xdf, 0xff, 0x2f, 0xf3, 0x14, 0x36, 0xc7, 0xd9, 0x57, 0x21, 0x73, 0x7c, 0x5e, 0xed, 0xa9
])

class TestDigest:
    def test_digest(self):
        assert item.digest(0, bytes(), bytes()) == emptyLeaf
        assert testLeaf == item.digest(1, bytes("key", "utf-8"), bytes("value", "utf-8"))