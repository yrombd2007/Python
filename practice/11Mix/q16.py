# Create a List of Squares of Odd Numbers Given:

l = [1, 2, 3, 4, 5, 6]
i = []
c = 0

while c < len(l):
    if l[c]%2!=0:
         i.append(l[c] * l[c])
    c+=1
print(i)