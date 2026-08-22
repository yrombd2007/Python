# Count Digits in a String Given:
s = "abc123xy45"
i = 0
c = 0

while c < len(s):
    if s[c].isdigit():
        i+=1
    c+=1
print(i)