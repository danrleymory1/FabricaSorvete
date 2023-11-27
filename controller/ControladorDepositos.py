from dao.daoDepositos import DepositoDAO
from model.Deposito import Deposito
from view.TelaDeposito import TelaDeposito


class ControladorDepositos:
    def __init__(self, controlador_sistema):
        self.__tela_deposito = TelaDeposito()
        self.__controlador_sistema = controlador_sistema
        self.__depositos_dao = DepositoDAO()

    @property
    def depositos_dao(self):
        return self.__depositos_dao

    def buscar_deposito(self):
        descricao = self.__tela_deposito.buscar()

        if descricao is None:
            return

        res = []

        for ing in self.__depositos_dao.get_all():
            if descricao.upper() in ing.descricao.upper():
                res.append(ing.__dict__)

        if len(res) == 0:
            self.__tela_deposito.mensagem_erro("Depósito não encontrado")
        else:
            self.__tela_deposito.info(res)

    def adicionar_deposito(self):
        depositos = [
            i.__dict__["_Deposito__descricao"] for i in self.__depositos_dao.get_all()
        ]

        descricao = self.__tela_deposito.adicionar(depositos)

        if descricao is None:
            return

        novo_deposito = Deposito(str(descricao))

        self.__depositos_dao.add(novo_deposito)

        self.__tela_deposito.mensagem_sucesso("Depósito adicionado com sucesso")

    def remover_deposito(self):
        depositos = [
            i.__dict__["_Deposito__descricao"] for i in self.__depositos_dao.get_all()
        ]

        descricao = self.__tela_deposito.remover(depositos)

        if descricao is None:
            return

        for ing in self.__depositos_dao.get_all():
            if ing.descricao == descricao:
                self.__depositos_dao.remove(ing)
                self.__tela_deposito.mensagem_sucesso("Depósito removido com sucesso")
                return

        self.__tela_deposito.mensagem_erro("Depósito não encontrado")

    def alterar_deposito(self):
        depositos = [
            i.__dict__["_Deposito__descricao"] for i in self.__depositos_dao.get_all()
        ]

        values = self.__tela_deposito.alterar(depositos)

        if values == None:
            return

        nova_descricao = values["descricao"]
        deposito = values["deposito"]

        for ing in self.__depositos_dao.get_all():
            if ing.descricao == deposito:
                ing.descricao = nova_descricao
                self.__depositos_dao.update(ing)
                self.__tela_deposito.mensagem_sucesso("Depósito alterado com sucesso")
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
        dict_list = []

        for dep in self.__depositos_dao.get_all():
            dict_list.append(dep.__dict__)

        self.__tela_deposito.info(dict_list)
