from exceptions.SabornoSistema import SabornoSistema
from model.Sabor import Sabor
from view.TelaSabor import TelaSabor


class ControladorSabores:
    def __init__(self):
        self.__sabores = []
        self.__tela_sabor = TelaSabor()

    def retornar_por_descricao(self, descricao: str):
        for sabor in self.__sabores:
            if sabor.descricao == descricao:
                return sabor
            return "Sabor não encontrado!"

    def adicionar_sabor(self):
        novo_sabor = self.__tela_sabor.adicionar_dados()
        descricao = novo_sabor["descricao"]
        sabor = self.retornar_por_descricao(descricao)
        try:
            if sabor is None:
                sabor = Sabor(novo_sabor["descricao"])
                self.__sabores.append(sabor)
            else:
                raise SabornoSistema
        except SabornoSistema as e:
            self.__tela_sabor.mostra_mensagem(e)

    def listar_sabores(self):
        for sabor in self.__sabores:
            self.__tela_sabor.mostrar_dados(
                {"codigo": sabor.codigo, "descricao": sabor.descricao}
            )

    def excluir_sabor(self):
        pass

    def alterar_sabor(self):
        self.listar_sabores()
        descricao = self.__tela_sabor.selecionar_dados()
        sabor = self.retornar_por_descricao(descricao)
        if sabor is not None:
            novo_sabor = self.__tela_sabor.adicionar_dados()
            sabor.descricao = novo_sabor["descricao"]
        else:
            self.__tela_sabor.mostra_mensagem("Sabor não encontrado!")

    def selecionar_dados(self):
        pass

    def abre_tela(self):
        pass


class ControladorSabors:
    def __init__(self):
        self.__sabores = []
        self.__tela_sabor = TelaSabor()

    def buscar_sabor(self):
        codigo = self.__tela_sabor.buscar_sabor()

        for sab in self.__sabores:
            if sab.codigo == codigo:
                self.__tela_sabor.sabor_info(sab)

        self.__tela_sabor.mensagem_erro("Sabor não encontrado")

    def adicionar_sabor(self):
        nome = self.__tela_sabor.novo_sabor()

        novo_ingrediente = Sabor(nome)

        self.__sabores.append(novo_ingrediente)

        self.__tela_sabor.mensagem_sucesso("Sabor adicionado com sucesso")

    def remover_sabor(self):
        codigo = self.__tela_sabor.remover_sabor()

        for ing in self.__sabores:
            if ing.codigo == codigo:
                self.__sabores.remove(ing)
                self.__tela_sabor.mensagem_sucesso("Sabor removido com sucesso")

        self.__tela_sabor.mensagem_erro("Sabor não encontrado")

    def alterar_sabor(self):
        (codigo, novo_nome) = self.__tela_sabor.alterar_sabor()

        for i, ing in enumerate(self.__sabores):
            if ing.codigo == codigo:
                self.__sabores[i].nome = novo_nome
                self.__tela_sabor.mensagem_sucesso("Sabor alterado com sucesso")

        self.__tela_sabor.mensagem_erro("Sabor não encontrado")
