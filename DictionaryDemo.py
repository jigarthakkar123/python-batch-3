d={111:"Vishnu",123:"Ashish",567:"Harsh",890:"Bansi"}

print(d)
print(d[123])
d1=d.copy()
print(d1)
print(d.get(567))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(123))
print(d.popitem())
d2={1:"Bansi",2:"Ashish",3:"Rajkuvarba",4:"Jigar"}
d.update(d2)
print(d)
for i in d:
    print(i," : ",d[i])

print(123 in d)
d[2]="Sunil"
print(d)
