l=[10,10.10,"python",True,10,1.11,"Java"]

print(l)
l.append(100)
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
l1.append(200)
print(l)
print(l1)
l2=l
print(l2)
l2.append(300)
print(l)
print(l2)
print(l.count(1))
l3=["Digital Marketing",101,1.90,"Automation"]
l.extend(l3)
print(l)
print(l.index(10,2))
print(l.pop())
print(l.pop(3))
l.remove(10)
print(l)
l.reverse()
print(l)
