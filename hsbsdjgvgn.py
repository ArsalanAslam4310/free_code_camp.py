def chunkey(lis,size):
    new=[]
    for i in range(size):
        if len(lis)//size:
            new.append(size)
    return new


lis=[6,6,54,3,22,2]
print(chunkey(lis,3))