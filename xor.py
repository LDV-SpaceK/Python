string = "label"
flag=""
for i in string:
    flag+=chr(ord(i)^13)

print(flag)
    