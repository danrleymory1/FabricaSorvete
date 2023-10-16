from model.Receita import Receita


class Sorvete:
    auto_codigo = 1

    def __init__(self, sabor, receita):
        self.__codigo = Sorvete.auto_codigo
        Sorvete.auto_codigo += 1
        self.__sabor = sabor
        self.__receita = receita
        self.__quantidade = 0

    @property
    def codigo(self):
        return self.__codigo

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

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
