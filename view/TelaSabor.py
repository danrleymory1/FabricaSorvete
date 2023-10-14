from Tela import Tela


class TelaSabor(Tela):
    def opcoes(self):
        print("-------- Sabor ----------")
        print("Escolha a opcao: ")
        print("1 - Adicionar Sabor")
        print("2 - Alterar Sabor")
        print("3 - Listar Sabores")
        print("4 - Excluir Sabor")
        print("0 - Retornar ao menu principal")
        opcao = self.opcao_input("Opcao = ", [0, 1, 2, 3, 4])
        return opcao

    def adicionar(self):
        print("---------- Novo Sabor ----------")
        descricao = input("Descricao = ")
        return descricao

    def info(self, sabor):
        print("---------- Sabor ----------")
        print("Codigo = ", sabor.codigo)
        print("Descricao = ", sabor.nome)

    def buscar(self):
        codigo = input("Código = ")
        return codigo
