from view.Tela import Tela


class TelaTransferencia(Tela):

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
        print("---------- Transferencia ---------")
        print("Escolha a opcao: ")
        print("1 - Transferir produto")
        print("2 - Listar Transferências")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opcao = ", [0, 1, 2])
        return opcao
