class Package():

    def __init__(self, name, version):
        self.__name = name
        self.__version = version
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def version(self):
        return self.__version
    
    @version.setter
    def version(self, version):
        self.__version = version

        