#  Find the Last Odd Number Given:
# l = [4, 8, 3, 6, 9, 12, 5]
# i=0
# c=0
# d=1
# while c<len(l):
#     if l[c]%2!=0:
#         i=l[c]
#         if l[d]:
#             if c<d: 
#                 i=l[d]
#     c+=1
# print(i)




l = [4, 8, 3, 6, 9, 12, 5]

i = 0
c = 0

while c < len(l):
    if l[c] % 2 != 0:
        i = l[c]

    c += 1

print(i)
