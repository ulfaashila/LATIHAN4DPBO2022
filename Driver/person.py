class person:

    def __init__(self):
        super().__init__()
        self.__NIK = ""
        self.__nama = ""
        self.__gender = ""
    
    #constructors
    def setperson(self,  NIK = "", nama = "", gender = ""):
        self.__NIK = NIK
        self.__nama = nama
        self.__gender = gender        
        
    #setter and getter 
    def setNIK(self, NIK):
        self.__NIK = NIK
    
    def getNIK(self):
        return self.__NIK
    
    def setnama(self, nama):
        self.__nama = nama
    
    def getnama(self):
        return self.__nama
    
    def setgender(self, gender):
        self.__gender = gender
    
    def getgender(self):
        return self.__gender
    
    # sleep
    def sleep(self):
        print(self.__nama + " is sleeping...")