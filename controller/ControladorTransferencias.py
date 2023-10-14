from view.TelaTransferencia import TelaTransferencia


class ControladorTransferencias:
    def __init__(self, controlador_sistema):
        self.__transferencias = []
        self.__controlador_sistema = controlador_sistema
        self.___tela_transferencia = TelaTransferencia()

    def retornar(self):
        self.__controlador_sistema.abrer_tela()

    def abre_tela(self):
        pass

