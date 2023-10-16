class Sabor:
    auto_codigo = 1

    def __init__(self, descricao: str):
        self.__codigo = Sabor.auto_codigo
        Sabor.auto_codigo += 1
        self.__descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
