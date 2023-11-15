from model.Receita import Receita
from model.Model import BaseModel


class Sorvete:
    def __init__(self, sabor, receita):
        super().__init__()
        self.__sabor = sabor
        self.__receita = receita
        self.__quantidade = 0

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
