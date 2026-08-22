# Check Number Palindrome
n = 12321
og=n
i=0
c=0
while n!=0:
    c=n%10
    n=n//10
    i=i*10+c
if i==og :
        print("yes")
else:
        print("no")






# og is use to not changed n in loop 