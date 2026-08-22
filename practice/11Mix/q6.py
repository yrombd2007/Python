# Remove Negative Numbers 
# Create a new list containing only the positive numbers.
l = [-3, 5, -1, 7, -8, 2]
i=[]
c=0

while c<len(l):
    if l[c]>0:
        i.append(l[c])
    c+=1
print(i)