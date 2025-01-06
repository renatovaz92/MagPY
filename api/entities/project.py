class Project():

    def __init__(self, name, packages):
        self.__name = name
        self.__packages = packages
        
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def packages(self):
        return self.__packages
    
    @packages.setter
    def packages(self, packages):
        self.__packages = packages
    