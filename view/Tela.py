from abc import ABC, abstractmethod


class Tela(ABC):
    @abstractmethod
    def tela_opcoes(self):
        pass

    # Para adicionar os métodos
    @abstractmethod
    def le_num_inteiro(self):
        pass

    @abstractmethod
    def selecionar_dados(self):
        pass

    @abstractmethod
    def mostrar_dados(self):
        pass

    @abstractmethod
    def adicionar_dados(self):
        pass
