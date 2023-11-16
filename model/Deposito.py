class Deposito:
    def __init__(self, descricao: str):
        super().__init__()
        self.__descricao = descricao
        self.__sorvetes = []

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
