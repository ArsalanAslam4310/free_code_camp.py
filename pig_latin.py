def pig_latin(string):
    
    for i in range(len(string)):
        if string[0]=="b,c,d,f,g,h,j,k,l,m,n,p,q,r,t,v,w,x,y,z":
            string+= string[0]+"ay"
        else:
            string+= string[0]+ "way"
            string=string.pop(0)

        return string

x="eight"
print(pig_latin(x))
