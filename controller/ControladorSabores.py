from exceptions.SabornoSistema import SabornoSistema
from model.Sabor import Sabor
from view.TelaSabor import TelaSabor


class ControladorSabores:
    def __init__(self, controlador_sistema):
        self.__sabores = []
        self.__tela_sabor = TelaSabor()
        self.__controla_sistema = controlador_sistema

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

    def retonar(self):
        self.__controla_sistema.abre_tela()

    def abre_tela(self):
        pass
