l = [1, -2, 3, -4, -5]

c = 0
i = 0

while c < len(l):
    if l[c] > 0:
        i += 1

    c += 1

print(i)