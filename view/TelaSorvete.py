from Tela import Tela


class TelaSorvete(Tela):
    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def tela_opcoes(self):
        print("-------- Sorvete ----------")
        print("Escolha a opcao: ")
        print("1 - Produzir Sorvete")
        print("2 - Listar Sorvetes")
        print("3 - Excluir Sorvete")
        print("0 - Retornar ao menu principal")
        opcao = self.le_num_inteiro("Opcao = ", [0, 1, 2, 3])
        return opcao

    def adicionar_dados(self):
        print("---------- Novo Sorvete ----------")
        preco = input("Preco = ")
        pass

    def mostrar_dados(self):
        pass

    def selecionar_dados(self):
        pass
