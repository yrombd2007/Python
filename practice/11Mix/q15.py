# Find the First Negative Number Given:
l = [5, 8, 3, -2, -7, 4]
i = 0
c = 0

while c < len(l):
    if l[c]<0:
        i=l[c]
        break
    c+=1
print(i)