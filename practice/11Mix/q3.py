# Sum Numbers Greater Than 5
l = [2, 7, 4, 9, 1, 8]
i=0
c=0
while c<len(l):
    if l[c]>5:
        i=i+l[c]
    c+=1
print(i)