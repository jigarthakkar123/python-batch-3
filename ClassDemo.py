'''
Main OOP Concepts:

1. class : It is a group of different type of variables & function.
2. object : It is an instance of class.
3. Inheritance : The object of one class can aquire the properties of object
of another class is called inheritance. or Creating a new class from an
exiting class is called inheritance.
Types of Inheritance

1. Single
2. Multilevel
3. Multiple
4. Hierarchy
5. Hybrid

4. Polymorphisam : One name multiple form.
    1. Compile Time(Method Overloading) : When there is a more than one method
    in a single class having the same name but with different number of
    arguments and their data types then it is called method overloading.
    2. Run Time(Method Overriding): When there is a same method prototype in
    your both base class & derived class & if you call that method using the
    object of derived class, then only derived class method will be called.
    So you can say that method of derived class overrides the method of base
    class.

5. Abstraction : To hide the data
6. Encapsulation : To bind a code & data in to a single unit is called
Encapsulation.
'''
class Student:

    def getData(self,fname,lname):
        print("getData Called")
        self.f=fname
        self.l=lname
    def putData(self):
        print("putData Called")
        print("First Name : ",self.f)
        print("Last Name : ",self.l)

s1=Student()
s2=Student()

s1.getData("Jigar","Thakkar")
s2.putData()











