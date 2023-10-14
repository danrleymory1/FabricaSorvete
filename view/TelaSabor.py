from view.Tela import Tela


class TelaSabor(Tela):
    def opcoes(self):
        print("-------- Sabor ----------")
        print("Escolha a opcao: ")
        print("1 - Adicionar Sabor")
        print("2 - Listar Sabor(es)")
        print("3 - Mostrar_sabor")
        print("4 - Alterar Sabor")
        print("5 - Excluir Sabor")
        print("0 - Retornar ao menu principal")
        opcao = self.opcao_input("Opcao = ", [0, 1, 2, 3, 4, 5])
        return opcao

    def adicionar(self):
        print("---------- Novo Sabor ----------")
        descricao = input("Descricao = ")
        return descricao

    def info(self, sabor):
        print("---------- Sabor ----------")
        print("Codigo: ", sabor.codigo)
        print("Descricao: ", sabor.nome)

    def buscar(self):
        print("---------- Buscar Sabor ----------")
        codigo = input("Código do Sabor a ser encontrado: ")
        return codigo

    def remover(self):
        print("---------- Remover Sabor ----------")
        codigo = input("Código do Sabor a ser removido: ")
        return codigo

    def alterar(self):
        print("---------- Alterar Sabor ----------")
        codigo = input("Código do Sabor a ser alterado: ")
        novo_nome = input("Novo nome: ")
        return codigo, novo_nome
