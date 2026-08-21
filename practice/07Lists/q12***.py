L=[1,2,3,4]
M=L[0]
i=0


while i<=len(L)-1:
    if M<=L[i]:
        M=L[i] 
    i+=1   
print("Max number=",M)
