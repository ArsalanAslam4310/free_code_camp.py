def mutation(lis):
    '''
    gdgt
    '''
    i = 0
    lis[i] = lis[i].lower()
    lis[i+1] = lis[i+1].lower()

    if lis[i] == lis[i+1]:
        return True
    else:
        return False


li = ["This", "this"]
print(mutation(li))
