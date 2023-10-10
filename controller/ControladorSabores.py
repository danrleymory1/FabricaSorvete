from model.Sabor import Sabor
from view.TelaSabor import TelaSabor


class ControladorSabores:
  def __init__(self, controlador_sistema):
    self.__sabores = []
    self.__tela_sabor = TelaSabor()
    self.__controla_sistema = controlador_sistema

  def retornar_por_codigo(self, codigo: int):
    for sabor in self.__sabores:
      if(sabor.codigo == codigo):
        return sabor
      return "Sabor não encontrado!"

  def adicionar_sabor(self):
    novo_sabor = self.__tela_sabor.adicionar_dados()
    descricao = novo_sabor["descricao"]
    
    
  def selecionar_dados(self):
    pass

  def retonar(self):
    self.__controla_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1. self.}
      
      
