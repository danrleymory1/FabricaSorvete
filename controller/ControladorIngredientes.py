from model.Ingrediente import Ingrediente
from view.TelaIngrediente import TelaIngrediente


class ControladorIngredientes:
    def __init__(self, controlador_sistema):
        self.__ingredientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_ingrediente = TelaIngrediente()

    def buscar_ingrediente(self):
        codigo = self.__tela_ingrediente.buscar()

        for ing in self.__ingredientes:
            if ing.codigo == codigo:
                self.__tela_ingrediente.info(ing)

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def adicionar_ingrediente(self):
        nome = self.__tela_ingrediente.adicionar()

        novo_ingrediente = Ingrediente(nome)

        self.__ingredientes.append(novo_ingrediente)

        self.__tela_ingrediente.mensagem_sucesso("Ingrediente adicionado com sucesso")

    def remover_ingrediente(self):
        codigo = self.__tela_ingrediente.remover()

        for ing in self.__ingredientes:
            if ing.codigo == codigo:
                self.__ingredientes.remove(ing)
                self.__tela_ingrediente.mensagem_sucesso(
                    "Ingrediente removido com sucesso"
                )

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def alterar_ingrediente(self):
        (codigo, novo_nome) = self.__tela_ingrediente.alterar()

        for i, ing in enumerate(self.__ingredientes):
            if ing.codigo == codigo:
                self.__ingredientes[i].nome = novo_nome
                self.__tela_ingrediente.mensagem_sucesso(
                    "Ingrediente alterado com sucesso"
                )

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_ingrediente,
                        2: self.buscar_ingrediente,
                        3: self.alterar_ingrediente,
                        4: self.remover_ingrediente,
                        0: self.retornar
                        }
