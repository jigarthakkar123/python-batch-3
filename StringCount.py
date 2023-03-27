s=input("Enter String : ")

wd=1
sp=0
ch=0
nb=0
sc=0

for i in s:
    if i.isspace():
        sp=sp+1
        wd=wd+1
    elif i.isalpha():
        ch=ch+1
    elif i.isnumeric():
        nb=nb+1
    else:
        sc=sc+1
        
print("Total Space : ",sp)
print("Total Character : ",ch)
print("Total Numbers : ",nb)
print("Total Words : ",wd)
print("Total Special Characters : ",sc)
