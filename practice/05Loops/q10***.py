n=int(input ("enter number"))
i=0
while n!=0:
    d=n%10
    if d>i:
        i=d


    n=n//10

print(i)   