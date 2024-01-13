import hashlib
import sys

SALT = "ckczppom"
PREFIX = "000000"

for i in range(10000000):
    if hashlib.md5(SALT + str(i)).hexdigest()[0:6] == PREFIX:
        print "The answer is:", i
        sys.exit()
