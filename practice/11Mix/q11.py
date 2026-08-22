# . Count Numbers Divisible by 3 Given:
l = [3, 7, 9, 12, 14, 18, 20]
i=0
c=0
while c<len(l):
    if l[c]%3==0:
        i+=1
    c+=1
print(i)