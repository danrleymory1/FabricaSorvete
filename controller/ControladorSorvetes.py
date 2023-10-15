from model.Sorvete import Sorvete
from view.TelaSorvete import TelaSorvete


class ControladorSorvetes:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_sorvetes = TelaSorvete()
        self.__sorvetes = []

    def buscar_sorvete(self):
        codigo = self.__tela_sorvetes.buscar()

        for sorv in self.__sorvetes:
            if sorv.codigo == codigo:
                self.__tela_sorvetes.info(sorv)
                return

        self.__tela_sorvetes.mensagem_erro("Sabor não encontrado")

    def adicionar_sorvete(self):
        (sabor_codigo, ingredientes) = self.__tela_sorvetes.adicionar()

        sabor = self.__controlador_sistema.sabores.buscar_por_codigo(sabor_codigo)
        receita = self.__controlador_sistema.receitas.nova_dict(ingredientes)

        novo_sorvete = Sorvete(sabor, receita)

        self.__sorvetes.append(novo_sorvete)

        self.__tela_sorvetes.mensagem_sucesso("Sabor adicionado com sucesso")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {}
