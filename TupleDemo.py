t=(1,2,10,1.1,2.2,[10,20,30],"tops",True,"python",1,2)

print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)

print(t[5])
t[5].append(40)
print(t[5])
