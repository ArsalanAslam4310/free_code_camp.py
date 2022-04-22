def missing_letter(string):
    '''
    find missing letter in string
    '''
    
    a_to_z="abcdefghijklmnopqrstuvwxyz"
    
    for char in a_to_z:
        if char not in string:
            return char
    return None

string_of_letters="abcdefghijklmnopqrstuvwxyz"
print(missing_letter(string_of_letters))
