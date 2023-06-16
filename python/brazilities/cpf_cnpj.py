from validate_docbr import CPF, CNPJ

class Document:
    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocumentCpf(document)
        elif(len(document)) == 14:
            return DocumentCnpj(document)
        else:
            raise ValueError("Invalid Document")

class DocumentCpf:
    def __init__(self, document):
        if(self.is_valid(document)):
            self._document = document
        else:
            raise ValueError("Invalid CPF")
        pass

    def is_valid(self, document):
        v = CPF()
        if(v.validate(document)):
            return True
        else:
            return False

    def format(self):
        v = CPF()
        return v.mask(self._document)

    def __str__(self) -> str:
        return self.format()


class DocumentCnpj:
    def __init__(self, document):
        if(self.is_valid(document)):
            self._document = document
        else:
            raise ValueError("Invalid CNPJ")
        pass

    def is_valid(self, document):
        v = CNPJ()
        if(v.validate(document)):
            return True
        else:
            return False

    def format(self):
        v = CNPJ()
        return v.mask(self._document)

    def __str__(self) -> str:
        return self.format()