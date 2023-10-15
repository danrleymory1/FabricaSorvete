from view.Tela import Tela


class TelaIngrediente(Tela):
    def opcoes(self):
        print("-------- Ingrediente ----------")
        print("Escolha a opção: ")
        print("1 - Adicionar ingrediente")
        print("2 - Listar ingrediente(s)")
        print("3 - Mostrar ingrediente")
        print("4 - Alterar ingrediente")
        print("5 - Excluir ingrediente")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5])
        return opcao

    def adicionar(self):
        print("---------- Novo Ingrediente ----------")
        descricao = input("Descricao = ")
        return descricao

    def info(self, ingrediente):
        print("---------- Ingrediente ----------")
        print("Codigo: ", ingrediente.codigo)
        print("Descricao: ", ingrediente.nome)

    def buscar(self):
        print("---------- Buscar Ingrediente ----------")
        codigo = input("Código do Ingrediente a ser encontrado: ")
        return codigo

    def remover(self):
        print("---------- Remover Ingrediente ----------")
        codigo = input("Código do Ingrediente a ser removido: ")
        return codigo

    def alterar(self):
        print("---------- Alterar Ingrediente ----------")
        codigo = input("Código do Ingrediente a ser alterado: ")
        novo_nome = input("Novo nome: ")
        return codigo, novo_nome
