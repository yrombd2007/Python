# Count Uppercase Characters Given:
s = "PyTHon ProGram"
i = 0
c = 0

while c < len(s):
    if s[c].isupper():
        i+=1
    c+=1
print(i)