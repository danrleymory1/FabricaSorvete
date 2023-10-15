from model.Deposito import Deposito


class Transferencia:
    auto_codigo = 1

    def __init__(self, descricao: str, deposito_dest: Deposito):
        self.__codigo = Transferencia.auto_codigo
        Transferencia.auto_codigo += 1
        self.__descricao = descricao
        self.__deposito_dest = deposito_dest
        self.__produtos = {}

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def deposito_dest(self):
        return self.__deposito_dest

    @deposito_dest.setter
    def deposito_dest(self, deposito_dest):
        self.__deposito_dest = deposito_dest

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, produtos):
        self.__produtos = produtos
