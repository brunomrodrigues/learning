import json

class Adress:

    def __init__(self, cep):
            self.cep          = cep
            self._street       = ""
            self._neighborhood = "" 

    def __str__(self):
         return json.dumps(self.__dict__)
    
    @property
    def street(self):
        return self._street 
    
    @street.setter
    def street(self, new_street):
        self._street = new_street

    @property
    def neighborhood(self):
        return self._neighborhood 
    
    @neighborhood.setter
    def neighborhood(self, new_neighborhood):
        self._neighborhood = new_neighborhood

