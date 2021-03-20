class schenok ():
    def __init__(self, poroda, colour,size):
        self.poroda=poroda
        self.colour=colour
        self.size=size

    def con(self):
        print("Спит постоянно")

    def zwyki(self):
        print("Лает")

class dog(schenok):
    def __init__(self, poroda, colour,size, gylaet, grizet_weschi,):
        super().__init__( poroda, colour,size)
        self.gylaet=gylaet
        self.grizet_weschi=grizet_weschi


    def gryaznyla(self):
        print("постоянно чумазый")

    def kotiki(self):
        print("Гоняет котов, зачем?!?!")

dog1=dog("Лабрадор","белый","очень большой, что с ним вообще происходит?)","Постоянно гуляет, сколько можно-то","все погрызла")
dog1.gryaznyla()
dog1.kotiki()
dog1.con()
dog1.zwyki()
print(dog1.poroda)
print(dog1.colour)
print(dog1.size)
print(dog1.gylaet)
print(dog1.grizet_weschi)