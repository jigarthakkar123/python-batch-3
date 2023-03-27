#Function With No Argument & No Return Value

def printLine():
    print("*"*50)

printLine()
print("Welcome To User Defined Function In Python")
printLine()

#Function With Argument & No Return Value

def add(a,b):
    print("Addition : ",a+b)

printLine()
add(10,20)
printLine()

#Function With Argument & With Return Value

def sub(a,b):
    return a-b

printLine()
#ans=sub(10,20)
print("Subtraction : ",sub(10,20))
printLine()
