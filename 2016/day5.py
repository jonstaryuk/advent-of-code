import binascii
import hashlib


def password(door_id):
    m = hashlib.md5()
    m.update(door_id.encode())

    i = 0
    n = 0
    while True:
        _m = m.copy()
        _m.update(str(i).encode())
        digest = binascii.hexlify(_m.digest()).decode()
        if digest[:5] == "00000":
            print(digest[5])
            n += 1
            if n == 8:
                return

        i += 1


if __name__ == '__main__':
    password("cxdnnyjw")
