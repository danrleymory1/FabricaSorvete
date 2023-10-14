from Sabor import Sabor
from model.Receita import Receita


class Sorvete:
    auto_codigo = 1
    def __init__(self, preco: float, sabor: Sabor, receita: Receita):
        self.__codigo = Sorvete.auto_codigo
        Sabor.auto_codigo += 1
        self.__preco = preco
        self.__sabor = sabor
        self.__receita = receita

    # checar o diagrama para consultar os erros
    @property
    def codigo(self):
        return self.__codigo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def sabor(self):
        return self.__sabor

    @sabor.setter
    def sabor(self, sabor):
        self.__sabor = sabor

    @property
    def receita(self):
        return self.__receita

    @receita.setter
    def receita(self, receita):
        self.__receita = receita
