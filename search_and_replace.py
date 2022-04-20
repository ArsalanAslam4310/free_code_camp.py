def search_and_replace(string, before, after):
    '''
    search and replace the value
    '''
    after = list(after)
    if before[0].isupper():
        after[0] = after[0].upper()
    else:
        after[0] = after[0].lower()
    after = ''.join(after)

    return string.replace(before, after)


print(search_and_replace("Let us get back to more Coding", "Coding", "algorithms"))
