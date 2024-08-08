key=list("ioprx")
for i in range(0,3):
    for j in range(4-i):
        if key[j]>key[j+1]:
            temp=key[j]
            key[j]=key[j+1]
            key[j+1]=temp
print("".join(key))
    
