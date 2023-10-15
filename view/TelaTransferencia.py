from view.Tela import Tela


class TelaTransferencia(Tela):
    def opcoes(self):
        print("---------- Transferência ---------")
        print("Escolha a opção: ")
        print("1 - Transferir produto")
        print("2 - Listar Transferências")
        print("3 - Mostrar Transferência")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opção = ", [0, 1, 2])
        return opcao

    def adicionar(self):
        print("---------- Nova Transferência  ----------")
        deposito = input("Depósito de destino = ")
        produtos = []

        while True:
            produtos.append([self.adicionar_produto()])
            continuar = input("Acrescentar novo produto? [S/N]")
            if not continuar == "S":
                break

        return deposito, produtos

    def adicionar_produto(self):
        print("---------- Transferir Produto  ----------")
        codigo = input("Código = ")
        quantidade = input("Quanidade = ")
        return codigo, quantidade

    def info(self, transferencia):
        print("---------- Transferência ----------")
        print("Codigo: ", transferencia.codigo)
        print("Código depósito: ", transferencia.deposito_destiono.codigo)
        for p in transferencia.produtos:
            print("--- Produto ---")
            print("Código: ", p.produto.codigo)
            print("Nome: ", p.produto.nome)
            print("Quantidade: ", p.quantidade)

    def buscar(self):
        print("---------- Buscar Transferência ----------")
        codigo = input("Código da Transferência a ser encontrada: ")
        return codigo

    def remover(self):
        print("---------- Remover Transferência ----------")
        codigo = input("Código da Transferência a ser removida: ")
        return codigo

    def alterar(self):
        return
