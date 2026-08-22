# Reverse the digits of a number, but only include the even digits.
n = 5839247
i=0
c=0
while n!=0:
    c=n%10
    n=n//10
    if c%2==0:
        i=i*10+c
print(i)