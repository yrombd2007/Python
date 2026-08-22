# Count a Specific Character
# Count how many times "a" appears in:
s = "banana"
i=0
c=0
while c<len(s):
    if s[c]=="a":
        i+=1
    c+=1
print(i)