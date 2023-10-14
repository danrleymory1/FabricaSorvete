from model.Deposito import Deposito
from view.TelaDeposito import TelaDeposito


class ControladorDepositos:
    def __init__(self):
        self.__depositos = []
        self.__tela_deposito = TelaDeposito()

    def buscar_deposito(self):
        codigo = self.__tela_deposito.buscar_deposito()

        for dep in self.__depositos:
            if dep.codigo == codigo:
                self.__tela_deposito.deposito_info(dep)

        self.__tela_deposito.mensagem_erro("Depósito não encontrado")

    def adicionar_deposito(self):
        descricao = self.__tela_deposito.novo_deposito()

        novo_deposito = Deposito(descricao)

        self.__depositos.append(novo_deposito)

        self.__tela_deposito.mensagem_sucesso("Novo depósito inserido")

    def remover_deposito(self):
        codigo = self.__tela_deposito.remover_deposito()

        for dep in self.__depositos:
            if dep.codigo == codigo:
                self.__depositos.remove(dep)
                self.__tela_deposito.mensagem_sucesso("Depósito removido")

        self.__tela_deposito.mensagem_erro("Erro: Depósito não encontrado")

    def alterar_deposito(self):
        (codigo, descricao) = self.__tela_deposito.alterar_deposito()

        for i, dep in enumerate(self.__depositos):
            if dep.codigo == codigo:
                self.__depositos[i].descricao = descricao
                self.__tela_deposito.mensagem_sucesso("Depósito alterado")

        self.__tela_deposito.mensagem_erro("Depósito não encontrado")
