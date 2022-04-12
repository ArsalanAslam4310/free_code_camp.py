def spinal_case(string):
    '''
    Make the string in spinal case
    '''
    string=string.lower()
    return string.replace(" ","-")

strings="My School Near My House"
print(spinal_case(strings))
