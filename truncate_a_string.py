def truncate_string(str, num):
    '''
    truncate string 
    '''
    str=str[0:num]
    str1=(str+"...")
    return str1

string="dbdsjkn dsnjks jsdnjksdnsk sdkndkn"
print(truncate_string(string,6))
