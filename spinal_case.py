def spinal_case(string):
    beginning = 0
    lis = []
    for i in range(len(string)-1):
        if string[i] == " " or string[i] == "_":
            return string.replace(string[i], '-').lower()
        elif string[i].isupper() and i != 0:
            lis.append(string[beginning:i])
            beginning = i
    if lis:
        return '-'.join(lis).lower()

    


string = "thisIsSpinalTap"
print(spinal_case(string))
