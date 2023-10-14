from model.Ingrediente import Ingrediente


class ControladorIngredientes:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__ingredientes = []

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def ingredientes(self):
        return self.__ingredientes

    @ingredientes.setter
    def ingredientes(self, ingredientes):
        self.__ingredientes = ingredientes

    def buscar_ingrediente(self, codigo):
        for ing in self.ingredientes:
            if ing.codigo == codigo:
                return ing

        return False

    def adicionar_ingrediente(self, novo_ingrediente):
        if not isinstance(novo_ingrediente, Ingrediente):
            # TODO: exception informando que o tipo está errado
            return
        for ing in self.ingredientes:
            if novo_ingrediente.codigo == ing.codigo:
                # TODO: exception informando que o ingrediente já existe
                return

        self.ingredientes.append(novo_ingrediente)

    def remover_ingrediente(self, codigo):
        for ing in self.ingredientes:
            if ing.codigo == codigo:
                self.ingredientes.remove(ing)
                return True

        return False

    def alterar_ingrediente(self, codigo, novo_ingrediente):
        for i, ing in enumerate(self.ingredientes):
            if ing.codigo == codigo:
                self.ingredientes[i] = novo_ingrediente
                return True

        return False
