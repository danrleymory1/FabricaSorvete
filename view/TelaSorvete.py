from view.Tela import Tela


class TelaSorvete(Tela):

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
        print("-------- Sorvete ----------")
        print("Escolha a opcao: ")
        print("1 - Produzir Sorvete")
        print("2 - Listar Sorvetes")
        print("3 - Excluir Sorvete")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opcao = ", [0, 1, 2, 3])
        return opcao
