from Tela import Tela


class TelaSabor(Tela):
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
        print("-------- Sabor ----------")
        print("Escolha a opcao: ")
        print("1 - Adicionar Sabor")
        print("2 - Alterar Sabor")
        print("3 - Listar Sabores")
        print("4 - Excluir Sabor")
        print("0 - Retornar ao menu principal")
        opcao = self.le_num_inteiro("Opcao = ", [0, 1, 2, 3, 4])
        return opcao

    def adicionar_dados(self):
        print("---------- Novo Sabor ----------")
        descricao = input("Descricao = ")
        return {"descricao": descricao}

    def mostrar_dados(self, dados_sabor):
        print("---------- Sabor ----------")
        print("Codigo = ", dados_sabor["codigo"])
        print("Descricao = ", dados_sabor["descricao"])

    def selecionar_dados(self):
        descricao = input("Digite o codigo do Sabor para selecionar: ")
        return descricao

    def mostra_mensagem(self, msg):
        print(msg)
