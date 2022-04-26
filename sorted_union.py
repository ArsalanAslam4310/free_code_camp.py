def unique(lis1,lis2,lis3):
    new=[]
    
    x=set(lis1+lis2+lis3)
    new.append(x)
    return new

s=[1, 3, 2]
d=[3,2,5,6]
f=[5,6,78,3]
print(unique(s,d,f))
