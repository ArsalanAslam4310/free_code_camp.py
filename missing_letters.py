def missing_letter(string):
    miss=[]
    a_to_z="abcdefghijklmnopqrstuvwxyz"
    for char in a_to_z:
        if char not in string:
            miss.append(char)
    return miss

stri="abd"
print(missing_letter(stri))
