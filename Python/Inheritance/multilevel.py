class Animal :
    def eating(self):
        print("Animal is eating food")

class Dog(Animal):
    def Bark(self):
        print("Dog is barking")

class Sparrow(Dog):
    def fly(self):
        print("It is Flying")

S = Sparrow()
S.eating()
S.Bark()
S.fly()