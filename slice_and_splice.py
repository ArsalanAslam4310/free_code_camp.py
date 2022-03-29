def franken_Splice(arr1, arr2, n):
    '''
    put the value at n index
    '''
    new=[]
    x=arr1+arr2
    x.insert(1,n)
    new.append(x)
    return new

li=[1,3,4]
li1=[5,6]
print(franken_Splice(li,li1,2))
