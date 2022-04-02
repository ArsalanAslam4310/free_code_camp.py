def title_case(string):
    string = list(string.lower())
    string[0] = string[0].upper()
    for i in range(len(string)):
        if string[i] == " ":
            string[i+1] = string[i+1].upper()

    return "".join(string)


string = "I'm a little tea pot"
print(title_case(string))
