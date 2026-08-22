# Count a Specific Digit
n = 1223452226
target = 2
i=0
c=0
while n!=0:
    c=n%10
    n=n//10
    if c==2:
        i+=1
print(i)
