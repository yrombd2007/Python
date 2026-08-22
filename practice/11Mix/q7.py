# Count Numbers Greater Than the Average
# Find the average of:
l = [2, 4, 6, 8, 10]
i=0
c=0
while c<len(l):
    if l[c]>0:
        i=i+l[c]
    c+=1
print(i)

a=i/len(l)
print(a)

d=0
b=0
while d<len(l):
    if l[d]>a:
        b+=1
    d+=1
print(b)
