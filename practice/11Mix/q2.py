l = [7, 9, 5, 8, 4, 2]
i=0
c=0
while c<len(l):
    if l[c]%2==0:
        i=l[c]
        break
    c+=1
print(i)