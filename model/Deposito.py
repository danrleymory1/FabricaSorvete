import uuid


class Deposito:
    def __init__(self, descricao: str):
        self.__codigo = uuid.uuid4()
        self.__descricao = descricao
        self.__sorvetes = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def sorvetes(self):
        return self.__sorvetes

    @sorvetes.setter
    def sorvetes(self, sorvetes):
        self.__sorvetes = sorvetes
