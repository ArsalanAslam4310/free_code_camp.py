def spinal_case(string):
    string=string.lower()

    for i in range(len(string)-1):
        if string[i]==" ":
            return string.replace("_","-")

strings="The_Andy_Griffith_Show"
print(spinal_case(strings))