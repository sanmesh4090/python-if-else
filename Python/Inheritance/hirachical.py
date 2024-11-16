class car:
    def Company(self):
        print("It is the Mahindra Car")

class Thar(car):
    def car1 (self,name,model,milage):
        name = self.name
        model = self.model
        milage = self.milage

    def print_info(self,name,model,milage):
        print("The Car name is ",name)
        print("The Car model is ",model)
        print("The Car milage is ",milage)

class Scorpio(car):
    def car2 (self):
        print("It is the Scripo car")
        print("The car model 2020")
        print("The car milage is 60km/hr")
s = Scorpio()
s.Company()
s.car2()
print("\n")
t = Thar()
t.Company()
t.print_info("Thar",2022,30)