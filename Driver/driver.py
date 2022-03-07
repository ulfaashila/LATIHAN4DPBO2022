from person import person
from job import job

class driver(person, job):

    def __init__(self):
        super().__init__()
        self.__lisenceId = ""
        self.__activeUntil = ""
        self.__vehicleType = ""
    
    #constructors
    def __init__(self,  NIK = "", nama = "", gender = "",  NIP = "", companyName = "", 
    position = "", lisenceId = "", activeUntil = "", vehicleType = ""):
        
        self.setperson(NIK, nama, gender)
        self.setjob(NIP, companyName, position)
        self.__lisenceId = lisenceId
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType
        
    #setter and getter
    def setlisenceId(self, lisenceId):
        self.__lisenceId = lisenceId
    
    def getlisenceId(self):
        return self.__lisenceId
    
    def setactiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    
    def getactiveUntil(self):
        return self.__activeUntil
    
    def setvehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
    
    def getvehicleType(self):
        return self.__vehicleType

    
    #menampilkan class
    def printDriver(self):
        print("============================")
        print("NIK            : " + self.getNIK())
        print("Nama           : " + self.getnama())
        print("Gender         : " + self.getgender())
        print("NIP            : " + self.getNIP())
        print("Company Name   : " + self.getcompanyName())
        print("Position       : " + self.getposition())
        print("Lisence ID     : " + str(self.getlisenceId()))
        print("Active Untill  : " + str(self.getactiveUntil()))
        print("Vehicle Type   : " + str(self.getvehicleType()))
        self.sleep()
        print()