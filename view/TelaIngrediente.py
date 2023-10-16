from view.Tela import Tela


class TelaIngrediente(Tela):
    def opcoes(self):
        print("-------- Ingrediente ----------")
        print("Escolha a opção: ")
        print("1 - Adicionar ingrediente")
        print("2 - Listar ingrediente(s)")
        print("3 - Mostrar ingrediente")
        print("4 - Alterar ingrediente")
        print("5 - Alterar quantidade de ingrediente")
        print("6 - Excluir ingrediente")
        print("0 - Retornar ao menu principal")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5, 6])
        return opcao

    def adicionar(self):
        print("---------- Novo Ingrediente ----------")
        descricao = input("Descricao = ")
        return descricao

    def info(self, ingrediente):
        print("---------- Ingrediente ----------")
        print("Codigo: ", ingrediente.codigo)
        print("Descricao: ", ingrediente.nome)
        print("Quantidade: ", ingrediente.quantidade)

    def buscar(self):
        print("---------- Buscar Ingrediente ----------")
        codigo = self.input_int("Código do Ingrediente a ser encontrado: ")
        return codigo

    def remover(self):
        print("---------- Remover Ingrediente ----------")
        codigo = self.input_int("Código do Ingrediente a ser removido: ")
        return codigo

    def alterar(self):
        print("---------- Alterar Ingrediente ----------")
        codigo = self.input_int("Código do Ingrediente a ser alterado: ")
        novo_nome = input("Novo nome: ")
        return codigo, novo_nome

    def alterar_quantidade(self):
        print("---------- Alterar Quantidade de Ingrediente ----------")
        codigo = self.input_int("Código do Ingrediente a ser alterado: ")
        nova_quantidade = self.input_int("Nova quantidade: ")
        return codigo, nova_quantidade
