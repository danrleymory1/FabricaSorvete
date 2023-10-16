from model.Deposito import Deposito
from view.TelaDeposito import TelaDeposito


class ControladorDepositos:
    def __init__(self, controlador_sistema):
        self.__depositos = []
        self.__tela_deposito = TelaDeposito()
        self.__controlador_sistema = controlador_sistema

    @property
    def depositos(self):
        return self.__depositos

    def buscar_deposito(self):
        codigo = self.__tela_deposito.buscar()

        for dep in self.__depositos:
            if dep.codigo == codigo:
                self.__tela_deposito.info(dep)
                return

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
                return

        self.__tela_deposito.mensagem_erro("Depósito não encontrado")

    def alterar_deposito(self):
        (codigo, descricao) = self.__tela_deposito.alterar()

        for i, dep in enumerate(self.__depositos):
            if dep.codigo == codigo:
                self.__depositos[i].descricao = descricao
                self.__tela_deposito.mensagem_sucesso("Depósito alterado")
                return

        self.__tela_deposito.mensagem_erro("Depósito não encontrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar_deposito,
            2: self.listar_depositos,
            3: self.buscar_deposito,
            4: self.alterar_deposito,
            5: self.remover_deposito,
            0: self.retornar,
        }
        while True:
            lista_opcoes[self.__tela_deposito.opcoes()]()

    def listar_depositos(self):
        self.__tela_deposito.mensagem("--- Depósitos ---")
        for dep in self.__depositos:
            self.__tela_deposito.info(dep)

    def buscar_por_codigo(self, codigo):
        for dep in self.__depositos:
            if dep.codigo == codigo:
                return dep

        return None
