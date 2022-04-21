def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(char) > 1:
        print("Invalid input!")
        return None
    if char in vowels:
        return True
    return False


def pig_latin(string):

    if is_vowel(string[0]):
        string += "way"
    else:
        fragment = ''
        for char in string:
            if not is_vowel(char):
                fragment += char
            else:
                break

        string = string.replace(fragment, '')
        string += fragment + "ay"

    return string


string = "schwartz"
print(pig_latin(string))
