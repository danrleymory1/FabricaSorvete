from Ingrediente import Ingrediente


class Receita:
    auto_codigo = 1

    def __init__(self, descricao: str, ingredientes: dict):
        self.__codigo = Receita.auto_codigo
        Receita.auto_codigo += 1
        self.__descricao = descricao
        # ingredientes

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
