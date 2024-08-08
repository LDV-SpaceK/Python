key=list("trknd")
temp=""
for i in range(2):
    temp=key[0 + i]
    key[0+i]=key[4 - i]
    key[4 - i]=temp

print("".join(key))
