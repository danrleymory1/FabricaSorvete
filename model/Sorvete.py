from Sabor import Sabor


class Sorvete:
    auto_codigo = 1

    def __init__(self, preco: float, sabor: Sabor, receita: None) -> None:
        self.__codigo = Sorvete.auto_codigo
        Sabor.auto_codigo += 1
        self.__preco = preco
        pass

    # checar o diagrama para consultar os erros

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo
