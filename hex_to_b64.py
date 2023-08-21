#!/usr/bin/env python3
import sys
import base64


def hex_to_b64(hex) -> str:

    arr = bytes.fromhex(hex)
    b64 = base64.b64encode(arr)
    print(b64.decode())
    return b64.decode()


if __name__ == '__main__':
    hex_to_b64(sys.argv[1])
