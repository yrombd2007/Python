# Count Elements at Even Indexes
# Count how many elements are at even indexes:
l = [10, 20, 30, 40, 50, 60]
i=0
c=0
while c<len(l):
    if l[c]:
        if c%2==0:
            i+=1
    c+=1
print(i)
