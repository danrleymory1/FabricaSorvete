from model.Sabor import Sabor
from view.TelaSabor import TelaSabor


class ControladorSabores:
    def __init__(self):
        self.__sabores = []
        self.__tela_sabor = TelaSabor()

    def buscar_sabor(self):
        codigo = self.__tela_sabor.buscar()

        for sab in self.__sabores:
            if sab.codigo == codigo:
                self.__tela_sabor.info(sab)

        self.__tela_sabor.mensagem_erro("Sabor não encontrado")

    def adicionar_sabor(self):
        nome = self.__tela_sabor.adicionar()

        novo_ingrediente = Sabor(nome)

        self.__sabores.append(novo_ingrediente)

        self.__tela_sabor.mensagem_sucesso("Sabor adicionado com sucesso")

    def remover_sabor(self):
        codigo = self.__tela_sabor.remover()

        for ing in self.__sabores:
            if ing.codigo == codigo:
                self.__sabores.remove(ing)
                self.__tela_sabor.mensagem_sucesso("Sabor removido com sucesso")

        self.__tela_sabor.mensagem_erro("Sabor não encontrado")

    def alterar_sabor(self):
        (codigo, novo_nome) = self.__tela_sabor.alterar()

        for i, ing in enumerate(self.__sabores):
            if ing.codigo == codigo:
                self.__sabores[i].nome = novo_nome
                self.__tela_sabor.mensagem_sucesso("Sabor alterado com sucesso")

        self.__tela_sabor.mensagem_erro("Sabor não encontrado")
