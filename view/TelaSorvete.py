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
        sabor = input("Sabor = ")
        ingredientes = {}
        print("--- Receita ---")

        while True:
            self.adicionar_ingrediente(ingredientes)

            continuar = input("Acrescentar novo ingrediente? [S/N] ")
            if not continuar == "S":
                break
        return sabor, ingredientes

    def adicionar_ingrediente(self, ingredientes_dict):
        codigo = input("Código do ingrediente = ")
        quantidade = input("Quantidade do ingrediente = ")
        ingredientes_dict[codigo] = quantidade

    def info(self, sorvete):
        print("---------- Sorvete ----------")
        print("Codigo: ", sorvete.codigo)
        print("Descricao: ", sorvete.sabor)

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
        novo_sabor = input("Novo sabor: ")
        return codigo, novo_sabor

    def produzir(self):
        print("---------- Alterar Sorvete ----------")
        codigo = input("Código do Sorvete a ser produzido: ")
        quantidade = input("Quantidade de sorvete a ser produzida: ")
        return codigo, quantidade
