l=[]

for i in range(1,1001):
    if i%7==0 and i%5!=0:
        l.append(i)

print(l)
print(len(l))
print(min(l))
print(max(l))
