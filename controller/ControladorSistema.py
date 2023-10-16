from controller.ControladorDepositos import ControladorDepositos
from controller.ControladorIngredientes import ControladorIngredientes
from controller.ControladorSorvetes import ControladorSorvetes
from controller.ControladorTransferencias import ControladorTransferencias
from view.TelaSistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_depositos = ControladorDepositos(self)
        self.__controlador_transferencias = ControladorTransferencias(self)
        self.__controlador_ingredientes = ControladorIngredientes(self)
        self.__controlador_sorvetes = ControladorSorvetes(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_depositos(self):
        return self.__controlador_depositos

    @property
    def controlador_transferencias(self):
        return self.__controlador_transferencias

    @property
    def controlador_ingredientes(self):
        return self.__controlador_ingredientes

    @property
    def controlador_sorvetes(self):
        return self.__controlador_sorvetes

    def inicializa_sistema(self):
        self.abre_tela()

    def sorvetes(self):
        self.__controlador_sorvetes.abre_tela()

    def ingredientes(self):
        self.__controlador_ingredientes.abre_tela()

    def depositos(self):
        self.__controlador_depositos.abre_tela()

    def transferencias(self):
        self.__controlador_transferencias.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mensagem("Saindo...")
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.sorvetes,
            2: self.ingredientes,
            3: self.transferencias,
            4: self.depositos,
            0: self.encerra_sistema,
        }
        while True:
            opcao_escolhida = self.__tela_sistema.opcoes()
            funcao_escolhida = lista_opcoes[opcaonn_escolhida]
            funcao_escolhida()
