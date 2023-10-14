from view.TelaSorvete import TelaSorvete


class ControladorSorvetes:
    def __init__(self, controlador_sistema):
        self.__sorvetes = []
        self.__tela_sorvetes = TelaSorvete()
        self.__controlador_sistema = controlador_sistema

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        pass
