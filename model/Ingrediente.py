class Ingrediente:
    auto_codigo = 1

    def __init__(self, nome: str):
        self.__nome = nome
        self.__quantidade = 0
        self.__codigo = self.__class__.auto_codigo
        self.__class__.auto_codigo += 1

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def __setstate__(self, d):
        self.__dict__ = d
        print(repr(d))

        if self.__class__.auto_codigo == None:
            self.__class__.auto_codigo = 1
        elif self.__class__.auto_codigo < self.codigo:
            self.__class__.auto_codigo = self.codigo + 1
