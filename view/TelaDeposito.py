from view.Tela import Tela


class TelaDeposito(Tela):
    def opcoes(self):
        print("-------- Depósito ----------")
        print("Escolha a opção: ")
        print("1 - Adicionar depósito")
        print("2 - Listar depósito(s)")
        print("3 - Mostrar depósito")
        print("4 - Alterar depósito")
        print("5 - Excluir depósito")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5])
        return opcao

    def adicionar(self):
        print("---------- Novo Depósito ----------")
        descricao = input("Descricao = ")
        return descricao

    def info(self, deposito):
        print("---------- Depósito ----------")
        print("Codigo: ", deposito.codigo)
        print("Descricao: ", deposito.nome)

    def buscar(self):
        print("---------- Buscar Depósito ----------")
        codigo = input("Código do Depósito a ser encontrado: ")
        return codigo

    def remover(self):
        print("---------- Remover Depósito ----------")
        codigo = input("Código do Depósito a ser removido: ")
        return codigo

    def alterar(self):
        print("---------- Alterar Depósito ----------")
        codigo = input("Código do Depósito a ser alterado: ")
        nova_descricao = input("Nova descrição: ")
        return codigo, nova_descricao
