class Receita:
    def __init__(self, descricao, ingredientes):
        self.__descricao = descricao
        self.__ingredientes = ingredientes

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def ingredientes(self):
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self, ingredientes):
        self.__ingredientes = ingredientes
