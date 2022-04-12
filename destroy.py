def destroyer(arr,*args):
    new=[]

    for i in range(len(arr)):
        arr.remove(*args)
        new.append(arr)
        return new

print(destroyer([1, 2, 3, 1, 2, 3],2))
