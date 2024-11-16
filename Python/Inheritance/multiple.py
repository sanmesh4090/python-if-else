class father():
    def name(self):
        print("It is the father ")

class mother():
    def mname(self):
        print("I am the mother")

class child(father,mother):
    def cname(self):
        print("i am the child")

c = child()
c.name()
c.mname()
c.cname()