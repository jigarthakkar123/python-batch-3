class Base:

    def show(self):
        print("Show From Base")

class Derived:

    def show(self):
        super().show()
        print("Show From Derived")

class SubDerived(Derived,Base):

    def show(self):
        super().show()
        print("Show From SubDerived")

d=SubDerived()
d.show()
