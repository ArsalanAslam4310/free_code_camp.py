def chunkey(lis,size):
    inner_list=[]
    outer_list=[]

    idx=0
    for _ in range(size):
        i=0
        while i<len(lis)//size:
            inner_list.append(lis[idx])
            idx+=1
            i+=1
        outer_list.append(inner_list)
        inner_list=[]
    return outer_list

lis=[6,6,54,3,22,2]
print(chunkey(lis,3))
