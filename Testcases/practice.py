class Parent:
    def __int__(self,fname,fage):
        self.name=fname
        self.age=fage
    def show(self):
        print("Name of my father is :-", self.name , "and the age is :-", self.age)


class child(Parent):
    def __int__(self, fname, fage):
        self.name = "James"
        self.age = 50

    def action(self):
        print("Name of my father is :-", self.name , "and the age is :-", self.age)


cd = child()
cd.show()
