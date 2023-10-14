from model.Deposito import Deposito
from view.TelaDeposito import TelaDeposito


class ControladorDepositos:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__depositos = []
        self.__tela_deposito = TelaDeposito()

    @property
    def depositos(self):
        return self.__depositos

    @depositos.setter
    def depositos(self, depositos):
        self.__depositos = depositos

    def buscar_deposito(self, codigo):
        for dep in self.depositos:
            if dep.codigo == codigo:
                return dep

        return False

    # WIP
    def adicionar_deposito(self, descricao):
        novo_deposito = self.__tela_deposito

        self.depositos.append(novo_deposito)

    def remover_deposito(self, codigo):
        for dep in self.depositos:
            if dep.codigo == codigo:
                self.depositos.remove(dep)
                return True

        return False

    def alterar_deposito(self, codigo, novo_deposito):
        for i, dep in enumerate(self.depositos):
            if dep.codigo == codigo:
                self.depositos[i] = novo_deposito
                return True

        return False
