from model.Ingrediente import Ingrediente
from view.TelaIngrediente import TelaIngrediente


class ControladorIngredientes:
    def __init__(self):
        self.__ingredientes = []
        self.__tela_ingrediente = TelaIngrediente()

    def buscar_ingrediente(self):
        codigo = self.__tela_ingrediente.buscar_ingrediente()

        for ing in self.__ingredientes:
            if ing.codigo == codigo:
                self.__tela_ingrediente.ingrediente_info(ing)

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def adicionar_ingrediente(self):
        nome = self.__tela_ingrediente.novo_ingrediente()

        novo_ingrediente = Ingrediente(nome)

        self.__ingredientes.append(novo_ingrediente)

        self.__tela_ingrediente.mensagem_sucesso("Ingrediente adicionado com sucesso")

    def remover_ingrediente(self):
        codigo = self.__tela_ingrediente.remover_ingrediente()

        for ing in self.__ingredientes:
            if ing.codigo == codigo:
                self.__ingredientes.remove(ing)
                self.__tela_ingrediente.mensagem_sucesso(
                    "Ingrediente removido com sucesso"
                )

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def alterar_ingrediente(self):
        (codigo, novo_nome) = self.__tela_ingrediente.alterar_ingrediente()

        for i, ing in enumerate(self.__ingredientes):
            if ing.codigo == codigo:
                self.__ingredientes[i].nome = novo_nome
                self.__tela_ingrediente.mensagem_sucesso(
                    "Ingrediente alterado com sucesso"
                )

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")
