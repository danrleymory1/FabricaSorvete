from model.Receita import Receita
import uuid


class Sorvete:
    def __init__(self, sabor, ingredientes_quantidades):
        super().__init__()
        self.__codigo = uuid.uuid4()
        self.__sabor = sabor
        self.__quantidade = 0
        self.__receita = Receita(ingredientes_quantidades)

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
