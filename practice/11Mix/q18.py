# Find the Sum of Numbers at Odd Indexes Given:
l = [10, 20, 30, 40, 50, 60]
i = 0
c = 0

while c < len(l):
    if c%2!=0:
        i=i+l[c]
    c+=1
print(i)