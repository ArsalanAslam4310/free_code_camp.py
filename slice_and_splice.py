def franken_Splice(arr1, arr2,n):
    '''
    put the value at n index
    '''
    new=[]

    for i in range(len(arr2)):
        new.append(arr2[i])
        for j in range(len(arr1)):
            n=arr1[j]
            new.append(n)
        new.append(arr2[i+1])
        return new

li=[1,2,3]
li1=[4,5]
print(franken_Splice(li,li1,1)) 
