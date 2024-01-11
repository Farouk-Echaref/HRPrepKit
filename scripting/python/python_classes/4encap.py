#!/usr/bin/python3

# "__" double underscore represents private attribute. 
# Private attributes start with "__".

class Base:
    def __init__(self) -> None:
        self.a = "public"
        self.__b = "private"
    def printPriv(self) -> None:
        print(self.__b)

class Derived(Base):
    def __init__(self) -> None:
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__b)

if __name__ == "__main__":
    bb = Base()
    # print(bb.a)
    # bb.printPriv()

    dd = Derived()