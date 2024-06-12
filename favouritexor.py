from Crypto.Util.number import *
cipher=(bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"))
for i in range(256):
    flag = [chr(i ^ j) for j in cipher]
    if "".join(flag).startswith("crypto"):
        print("".join(flag))
