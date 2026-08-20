n=int(input ("enter number"))
i=1
while n!=0:
    i=i*(n%10)
    n=n//10

print(i)   