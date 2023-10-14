from view.Tela import Tela


class TelaSistema(Tela):
    def buscar(self):
        pass

    def info(self, objeto):
        pass

    def adicionar(self):
        pass

    def remover(self):
        pass

    def alterar(self):
        pass

    def opcoes(self):
        print("---------- IceFac ----------")
        print("Escolha uma das opções abaixo: ")
        print("1. Sabor")
        print("2. Sorvete")
        print("3. Ingrediente")
        print("4. Transferencia")
        print("5. Deposito")
        print("0. Finalizar")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5])
        return opcao
