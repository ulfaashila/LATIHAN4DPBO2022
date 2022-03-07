class vehicle:

    def __init__(self):
        super().__init__()
        self.__name = ""
        self.__fuelType = ""
        self.__MaxPass = ""
        self.__type = ""
        self.__age = ""
    
    #constructors
    def setvehicle(self, name = "", fuelType = "", MaxPass = "", type = "", age = ""):
        self.__name = name
        self.__fuelType = fuelType
        self.__MaxPass = MaxPass
        self.__type = type
        self.__age = age
        
    # getter and setter
    def setname(self, name):
        self.__name = name
    
    def getname(self):
        return self.__name
    
    def setfuelType(self, fuelType):
        self.__fuelType = fuelType
    
    def getfuelType(self):
        return self.__fuelType

    def setMaxPass(self, MaxPass):
        self.__MaxPass = MaxPass
    
    def getMaxPass(self):
        return self.__MaxPass
    
    def settype(self, type):
        self.__type = type
    
    def gettype(self):
        return self.__type
    
    def setage(self, age):
        self.__age = age
    
    def getage(self):
        return self.__age
    
    # move method 
    def Move(self):
        print(self.__name + " is moving. . .")