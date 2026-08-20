n=int(input ("enter number"))
i=0
while n!=0:
    d=n%10
    if d==0:
        i="yes"
        break
    else:
        i="no"
   

    n=n//10

print(i)   