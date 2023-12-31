import datetime


class Transferencia:
    def __init__(self, deposito_dest, produtos):
        super().__init__()
        self.__deposito_dest = deposito_dest
        self.__produtos = produtos
        self.__data = datetime.datetime.now()

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

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
