class job:

    def __init__(self):
        super().__init__()
        self.__NIP= ""
        self.__companyName = ""
        self.__position = ""
    
    #constructors
    def setjob(self, NIP= "", companyName = "", position = ""):
        self.__NIP= NIP
        self.__companyName = companyName
        self.__position = position         
        
    #setter and getter
    def setNIP(self, NIP):
        self.__NIP= NIP
    
    def getNIP(self):
        return self.__NIP

    def setcompanyName(self, companyName):
        self.__companyName = companyName
    
    def getcompanyName(self):
        return self.__companyName
    
    def setposition(self, position):
        self.__position = position
    
    def getposition(self):
        return self.__position