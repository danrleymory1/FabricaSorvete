class Receita:
    def __init__(self):
        self.__ingredientes_e_quantidades = []

    @property
    def ingredientes_e_quantidades(self):
        return self.__ingredientes_e_quantidades

    @ingredientes_e_quantidades.setter
    def ingredientes_e_quantidades(self, ingredientes_e_quantidades):
        self.__ingredientes_e_quantidades = ingredientes_e_quantidades

    def adicionar_ingrediente_e_quantidade(self, ingrediente, quantidade):
        i = dict()
        i["ingrediente"] = ingrediente
        i["quantidade"] = quantidade

        self.ingredientes_e_quantidades.append(i)
