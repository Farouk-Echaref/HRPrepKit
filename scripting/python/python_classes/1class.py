#!/usr/bin/python3

class testing:
    def __init__(self, name: str, age: int, pos: str) -> None:
        self.name = name
        self.age = age
        self.pos = pos
    def print_attr(self) -> None:
        print(self.name, self.age, self.pos)

class second:
    def __init__(self, val: int) -> None:
        self.val = val
    def getVal(self) -> int:
        return (self.val)


if __name__ == "__main__":
    obj = testing("fech", 24, "intern")
    sc = second(42)

    obj.print_attr()
    print(sc.getVal())