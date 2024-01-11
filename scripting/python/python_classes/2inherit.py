#!/usr/bin/python3
# demonstrate how parent and child constructors are invoked

class Parent:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def display(self) -> None:
        print(self.name)
        print(self.id)

    def details(self) -> None:
        print("Name is {}".format(self.name))
        print("ID is {}".format(self.id))

#child class inheriting from Parent
class Child(Parent):
    def __init__(self, name: str, id: int, age: int, pos: str) -> None:
        self.age = age
        self.pos = pos

        #invoking the parent constructor 
        Parent.__init__(self, name, id)

    def details(self) -> None:
        print("Name is {}".format(self.name))
        print("ID is {}".format(self.id))
        print("Age is {}".format(self.age))
        print("Pos is {}".format(self.pos))

if __name__ == "__main__":
    chld = Child("fech", 1, 24, "intern")

    chld.display()
    chld.details()