from view.Tela import Tela


class TelaSistema(Tela):
    def buscar(self):
        return

    def info(self, objeto):
        return

    def adicionar(self):
        return

    def remover(self):
        return

    def alterar(self):
        return

    def opcoes(self):
        super().limpar_tela()
        print("---------- IceFac ----------")
        print("Escolha uma das opções abaixo: ")
        print("1 - Sorvete")
        print("2 - Ingrediente")
        print("3 - Transferencia")
        print("4 - Deposito")
        print("0 - Finalizar")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5])
        return opcao
