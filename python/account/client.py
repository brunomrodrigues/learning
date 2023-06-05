class Client:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, new_name):
        self.__name = new_name
        return self.name