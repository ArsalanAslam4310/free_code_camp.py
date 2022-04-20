def pig_latin(string):
    string=list(string)
    
    
    if string[0]=="a,e,i,o,u,s":
        string+= string[0]+"way"
        string=string.pop(0)
    else:
        string+= string[0]+ "ay"
        string.pop(0)
    string = ''.join(string)
    return string

string="paragraphs"
print(pig_latin(string))
