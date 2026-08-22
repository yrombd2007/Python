# Count Even and Odd Digits
n = 5839247
e=0
c=0
o=0
while n!=0:
    c=n%10
    if c%2==0:
        e+=1
    elif c%2!=0:
        o+=1
    n=n//10
print("even",e)
print("odd",o)

