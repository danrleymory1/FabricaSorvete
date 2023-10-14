from view.TelaSistema import TelaSistema
from controller.ControladorDepositos import ControladorDepositos
from controller.ControladorTransferencias import ControladorTranferencias
from controller.ControladorIngredientes import ControladorIngredientes
from controller.ControladorSorvetes import ControladorSorvetes
from controller.ControladorSabores import ControladorSabores


class ControladorSistema:
  def __init__(self):
    self.__tela_sistema = TelaSistema()
    self.__controlador_depositos = ControladorDepositos
    self.__controlador_transferencias = ControladorTranferencias
    self.__controlador_ingredientes = ControladorIngredientes
    self.__controlador_sorvetes = ControladorSorvetes
    self.__controlador_sabores = ControladorSabores
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

  @property
  def controlador_sabores(self):
    return self.__controlador_sabores
  
  def inicializa_sistema(self):
      self.abre_tela()

  def encerra_sistema(self):
    exit(0)

  def abre_tela(self):
      pass
    