import PySimpleGUI as sg
from view.Tela import Tela


class TelaTransferencia(Tela):
    def opcoes(self):
        print("---------- Transferência ---------")
        print("Escolha a opção: ")
        print("1 - Transferir produto")
        print("2 - Listar Transferências")
        print("3 - Mostrar Transferência")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3])
        return opcao

    def adicionar(self):
        print("---------- Nova Transferência  ----------")
        deposito = self.input_int("Depósito de destino = ")
        produtos = {}

        while True:
            self.adicionar_produto(produtos)

            continuar = input("Acrescentar novo produto? [S/N] ")
            if not continuar == "S":
                break

        return deposito, produtos

    def adicionar_produto(self, produtos_dict):
        codigo = self.input_int("Código do produto = ")
        quantidade = self.input_int("Quantidade do produto = ")
        produtos_dict[codigo] = quantidade

    def info(self, transferencia):
        print("---------- Transferência ----------")
        print("Codigo: ", transferencia.codigo)
        print("Código depósito: ", transferencia.deposito_dest.codigo)
        print("Data: ", transferencia.data)
        for cod, qtd in transferencia.produtos.items():
            print("--- Produto ---")
            print("Código: ", cod)
            print("Quantidade: ", qtd)

    def buscar(self):
        print("---------- Buscar Transferência ----------")
        codigo = self.input_int("Código da Transferência a ser encontrada: ")
        return codigo

    def remover(self):
        print("---------- Remover Transferência ----------")
        codigo = self.input_int("Código da Transferência a ser removida: ")
        return codigo

    def alterar(self):
        return
