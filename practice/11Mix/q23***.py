# Reverse a Number
n = 123456
i=0
c=0
while n!=0:
    c=n%10
    i = i * 10 + c
    n=n//10
print(i)