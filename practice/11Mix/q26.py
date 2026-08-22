# Find the Largest Digit
n = 5839247
i=0
c=0
while n!=0:
    c=n%10
    n=n//10
    if i<c:
        i=c
print(i)