from view.TelaSistema import TelaSistema
from controller.ControladorDepositos import ControladorDepositos
from controller.ControladorTransferencias import ControladorTranferencias
from controller.ControladorIngredientes import ControladorIngredientes
from controller.ControladorSorvetes import ControladorSorvetes
from controller.ControladorSabores import ControladorSabores


class ControladorSistema:
  def __init__(self):
    self.__controlador_depositos = ControladorDepositos(self)
    self.__controlador_transferencias = ControladorTranferencias(self)
    self.__controlador_ingredientes = ControladorIngredientes(self)
    self.__controlador_sorvetes = ControladorSorvetes(self)
    self.__controlador_sabores = ControladorSabores(self)
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

  def cadastra_sabores(self):
    self.__controlador_sabores.abre_tela()

  def cadastra_sorvetes(self):
    self.__controlador_sorvetes.abre_tela()

  def cadastra_ingredientes(self):
    self.__controlador_ingredientes.abre_tela()
  
  def cadastra_depositos(self):
    self.__controlador_depositos.abre_tela()
    
  def cadastra_transferencias(self):
    self.__controlador_transferencias.abre_tela()  

  def encerra_sistema(self):
    exit(0)

  def abre_tela(self):
    lista_opcoes = {1: self.cadastra_sabores,
                    2: self.cadastra_sorvetes,
                    3: self.cadastra_ingredientes,
                    4: self.cadastra_transferencias,
                    5: self.cadastra_depositos,
                    0: self.encerra_sistema}
    while True:
      opcao_escolhida = self.__tela_sistema.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()