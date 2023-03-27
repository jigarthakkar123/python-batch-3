import UDF

while True:

    print("****************")
    print("1. MaxOfTwo")
    print("2. MaxOfThree")
    print("3. Fibonacci")
    print("4. Prime")
    print("5. Exit")
    print("****************")
    
    choice=int(input("Enter Your Choice : "))
    print("****************")

    if choice==1:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        UDF.maxoftwo(a,b)
        print("****************")
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        UDF.maxofthree(a,b,c)
        print("****************")
    elif choice==3:
        c=int(input("Enter Value : "))
        UDF.fibonacci(c)
        print("****************")
    elif choice==4:
        c=int(input("Enter Value : "))
        UDF.prime(c)
        print("****************")
    else:
        print("Thank You Using Our Services. Good Bye")
        break
        
        
