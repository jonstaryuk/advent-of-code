import binascii
import hashlib


def password(door_id):
    m = hashlib.md5()
    m.update(door_id.encode())

    i = -1
    n = 0
    password = bytearray(8)
    while True:
        i += 1
        _m = m.copy()
        _m.update(str(i).encode())
        digest = binascii.hexlify(_m.digest()).decode()

        if digest[:5] == "00000":
            try:
                pos = int(digest[5])
            except ValueError:
                continue

            if not 0 <= pos < 8:
                continue

            if password[pos] != 0:
                continue

            password[pos] = ord(digest[6])
            print(password)
            n += 1

            if n == 8:
                return

        if i % 1000000 == 0:
            print("--", i)


if __name__ == '__main__':
    # password("abc")
    password("cxdnnyjw")

