from model.Deposito import Deposito
from view.TelaDeposito import TelaDeposito


class ControladorDepositos:
    def __init__(self):
        self.__depositos = []
        self.__tela_deposito = TelaDeposito()

    def buscar_deposito(self):
        codigo = self.__tela_deposito.buscar()

        for dep in self.__depositos:
            if dep.codigo == codigo:
                self.__tela_deposito.info(dep)

        self.__tela_deposito.mensagem_erro("Depósito não encontrado")

    def adicionar_deposito(self):
        descricao = self.__tela_deposito.adicionar()

        novo_deposito = Deposito(descricao)

        self.__depositos.append(novo_deposito)

        self.__tela_deposito.mensagem_sucesso("Novo depósito adicionado")

    def remover_deposito(self):
        codigo = self.__tela_deposito.remover()

        for dep in self.__depositos:
            if dep.codigo == codigo:
                self.__depositos.remove(dep)
                self.__tela_deposito.mensagem_sucesso("Depósito removido")

        self.__tela_deposito.mensagem_erro("Erro: Depósito não encontrado")

    def alterar_deposito(self):
        (codigo, descricao) = self.__tela_deposito.alterar()

        for i, dep in enumerate(self.__depositos):
            if dep.codigo == codigo:
                self.__depositos[i].descricao = descricao
                self.__tela_deposito.mensagem_sucesso("Depósito alterado")

        self.__tela_deposito.mensagem_erro("Depósito não encontrado")
