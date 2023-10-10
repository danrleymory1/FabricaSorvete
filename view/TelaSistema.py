from Tela import Tela


class TelaSistema(Tela):
  def adicionar_dados(self):
    pass

  def selecionar_dados(self):
    pass

  def mostrar_dados(self):
    pass

  def le_num_inteiro(self, mensagem=" ", ints_validos=None):
    while True:
      valor_lido = input(mensagem)
      try:
        valor_int = int(valor_lido)
        if ints_validos and valor_int not in ints_validos:
          raise ValueError
        return valor_int
      except ValueError:
        print("Valor incorreto!")
        if ints_validos:
          print("Valores válidos: ", ints_validos)

  def tela_opcoes(self):
    print("---------- IceFac ----------")
    print("Escolha uma das opções abaixo: ")
    print("1. Sabor")
    print("2. Sorvete")
    print("3. Ingrediente")
    print("4. Transferencia")
    print("5. Deposito")
    print("0. Finalizar")
    opcao = self.le_num_inteiro("Opção = ", [0, 1, 2, 3, 4, 5])
    return opcao