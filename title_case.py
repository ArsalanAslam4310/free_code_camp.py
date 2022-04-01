def title_case(string):
    string=string.lower()
    for i in range(len(string)):
        if string[i] == " ":
            string[i+1].upper()
    return string

string="I'm a little tea pot"
print(title_case(string))

