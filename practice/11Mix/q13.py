# Multiply Numbers Less Than 5 Given:
l = [2, 7, 3, 4, 8, 1]
i = 1
c = 0

while c < len(l):
    if l[c]<5 :
        i=i*l[c]
    c+=1
print(i)