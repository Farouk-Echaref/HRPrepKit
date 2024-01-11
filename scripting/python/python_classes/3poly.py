#!/usr/bin/python3

class Animal:
    def intro(self) -> None:
        print("Introducing Animals")
    def voice(self) -> None:
        print("Random Voice")

class Cat(Animal):
    def intro(self) -> None:
        print("Im Cat")
    def voice(self) -> None:
        print("Meow")

if __name__ == "__main__":
    cat = Cat()
    cat.intro()
    cat.voice()
