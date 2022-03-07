from vehicle import vehicle

class ship(vehicle):

    def __init__(self):
        super().__init__()
        self.__country = ""
    
    # constructors
    def __init__(self, name = "", fuelType = "", MaxPass = "", type = "", age = "", country = ""):
        self.setvehicle(name, fuelType, MaxPass, type, age)
        self.__country = country
        
    # getter and setter
    def setcountry(self, country):
        self.__country = country
    
    def getcountry(self):
        return self.__country
    
    # print class
    def printShip(self):
        print("=======")
        print("Name Ship                : " + self.getname())
        print("Fuel Type                : " + self.getfuelType())
        print("Max Passenger            : " + self.getMaxPass())
        print("Type                     : " + self.gettype())
        print("Age                      : " + self.getage())
        print("Country of Manufacture   : " + str(self.getcountry()))
        self.Move()
        print()