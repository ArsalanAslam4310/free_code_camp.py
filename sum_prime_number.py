number=int(input("Enter a number"))
sum=0
for num in range(0,number+1):
    i=1
    for i in range(2,num):
        if(int(num%i==0)):
            i=num
            break

    if i is not num:
        sum+=num
print(sum)
