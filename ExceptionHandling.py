'''
An abnormal situation that arises during the runtime of a program i called
Exception
'''
print("Start Code")
try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))

    c=a/b
    print("Division : ",c)
    l=[1,2,3,4,5,6]
    index=int(input("Enter Index Number To Print Element : "))
    print(l[index])
except + as e:
    print("Exception Caught : ",e)

print("End Code")
