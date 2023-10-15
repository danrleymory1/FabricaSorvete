from view.Tela import Tela


class TelaSorvete(Tela):
    def opcoes(self):
        print("-------- Sorvete ----------")
        print("Escolha a opção: ")
        print("1 - Produzir sorvete")
        print("2 - Adicionar sorvete")
        print("3 - Listar sorvete(es)")
        print("4 - Mostrar sorvete")
        print("5 - Alterar sorvete")
        print("6 - Excluir sorvete")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5])
        return opcao

    def adicionar(self):
        print("---------- Novo Sorvete ----------")
        descricao = input("Descricao = ")
        return descricao

    def info(self, sorvete):
        print("---------- Sorvete ----------")
        print("Codigo: ", sorvete.codigo)
        print("Descricao: ", sorvete.nome)

    def buscar(self):
        print("---------- Buscar Sorvete ----------")
        codigo = input("Código do Sorvete a ser encontrado: ")
        return codigo

    def remover(self):
        print("---------- Remover Sorvete ----------")
        codigo = input("Código do Sorvete a ser removido: ")
        return codigo

    def alterar(self):
        print("---------- Alterar Sorvete ----------")
        codigo = input("Código do Sorvete a ser alterado: ")
        novo_nome = input("Novo nome: ")
        return codigo, novo_nome

    def produzir(self):
        print("---------- Alterar Sorvete ----------")
        codigo = input("Código do Sorvete a ser produzido: ")
        quantidade = input("Quantidade de sorvete a ser produzida: ")
        return codigo, quantidade
