from pickle import FALSE

def mutation(lis):

    for i in range(0,len(lis)-1):
        lis[i] = lis[i].lower()
        if lis[i] == lis[i+1]:
            return True
        else:
            return False

li = ["This", "this"]
print(mutation(li))
