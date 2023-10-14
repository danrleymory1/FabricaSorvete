class Deposito:
    auto_codigo = 1

    def __init__(self, descricao: str):
        self.__codigo = Deposito.auto_codigo
        Deposito.auto_codigo += 1
        self.__descricao = descricao
        self.sorvetes = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def sorvetes(self):
        return self.__sorvetes

    @sorvetes.setter
    def sorvetes(self, sorvetes):
        self.__sorvetes = sorvetes
