class Sabor:
    auto_codigo = 1
    def __init__(self, nome: str):
        self.__codigo = Sabor.auto_codigo
        Sabor.auto_codigo += 1
        self.__nome = nome
        
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome