#!/usr/bin/python3

class Testing:
    def __init__(self, name: str, age: int, pos: str) -> None:
        self.name = name
        self.age = age
        self.pos = pos
    def print_attr(self) -> None:
        print(self.name, self.age, self.pos)

class Second:
    def __init__(self, val: int) -> None:
        self.val = val
    def getVal(self) -> int:
        return (self.val)
    def printVal(self) -> None:
        print("my val is {}".format(self.val))

class Fech:
    #class attribute
    name = "farouk"

    #instance attribute
    def __init__(self, login : str) -> None:
        self.login = login


if __name__ == "__main__":
    obj = Testing("fech", 24, "intern")
    sc = Second(42)
    fch = Fech("fech-cha")

    obj.print_attr()
    sc.printVal()

    #accessing class attributes
    print(fch.__class__.name)

    #accessing instance attributes
    print(fch.login)