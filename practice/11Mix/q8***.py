# Find the Difference Between Largest and Smallest
# Without using max() or min():
l = [4, 9, 2, 7, 5]

i = 0
c = l[0]

while i < len(l):
    if c > l[i]:
        c = l[i]

    i += 1

print(c)

i = 0
d = l[0]

while i < len(l):
    if d < l[i]:
        d = l[i]

    i += 1

print(d)

print(d - c)