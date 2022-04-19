def search_and_replace(string,exist,new_occurence):
    '''
    search and replace the value
    '''
    for i in range(len(new_occurence)):
        new_occurence[0]=new_occurence[0].upper()
        x=string.replace(exist,new_occurence)
    return x

string="Let us get back to more coding"
print(search_and_replace(string,"coding","algorithms"))
