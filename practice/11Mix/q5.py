# find the First Character That Is a Digit
s = "abc4xyz"

i = 0
c = 0

while c < len(s):
    if s[c].isdigit():
        i = c
        break

    c += 1

print(i)