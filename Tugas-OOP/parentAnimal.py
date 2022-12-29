#class
#parent
class Animal :
    def __init__(self, nama) :
        self.nama = nama
        
    def printAnimal(self):
        print(self.nama)
        

#child
class FullAnimal(Animal):
    def __init__(self, nama, vertebrata, makan, hidup):
        super().__init__(nama)
        self.vertebrata = vertebrata
        self.makan = makan
        self.hidup = hidup
        
    def printFullAnimal(self):
        print("Ini", self.nama, "adalah binatang", self.vertebrata, ", mereka hidup di", self.hidup, "mereka adalah binatang", self.makan)
