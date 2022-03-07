from vehicle import vehicle

class airplane(vehicle):
    
    # constructors
    def __init__(self, name = "", fuelType = "", MaxPass = "", type = "", age = "", wings = ""):
        self.setvehicle(name, fuelType, MaxPass, type, age)
        self.__wings = wings
        
    # getter and setter
    def setwings(self, wings):
        self.__wings = wings
    
    def getwings(self):
        return self.__wings
    
    # print class
    def printAirplane(self):
        print("============")
        print("Name Airplane            : " + self.getname())
        print("Fuel Type                : " + self.getfuelType())
        print("Max Passenger            : " + self.getMaxPass())
        print("Type                     : " + self.gettype())
        print("Age                      : " + self.getage())
        print("Wings Length             : " + str(self.getwings()))
        self.Move()
        print()