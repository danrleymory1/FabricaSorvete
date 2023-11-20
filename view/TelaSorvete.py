from view.Tela import Tela
import PySimpleGUI as sg


class TelaSorvete(Tela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def opcoes(self):
        self.init_opcoes()
        event, button = self.open()
        opcao = 0
        if event == 1:
            opcao = 1
        if event == 2:
            opcao = 2
        if event == 3:
            opcao = 3
        if event == 4:
            opcao = 4
        if event == 5:
            opcao = 5
        if event == 6:
            opcao = 6
        if event == 0 or button in (None, 'Retornar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def open(self):
        event, button = self.__window.Read()
        return event, button

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal')
        layout = [
            [sg.Text("Sorvete", font=("Bahnschrift", 21))],
            [sg.Text("Escolha uma das opções abaixo:", font=("Bahnschrift", 15), text_color="white")],
            [sg.Button("Produzir Sorvete", key=1, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Adicionar Sorvete", key=2, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Listar Sorvete(s)", key=3, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Mostrar Sorvete", key=4, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Alterar Sorvete", key=5, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Excluir Sorvete", key=6, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Column([[sg.Cancel("Retornar", key=0)]], justification='center')]
        ]

        column = sg.Column(layout, justification='center', element_justification='center',
                           vertical_alignment='center')

        # Layout com a coluna centralizada
        layout = [[column]]

        self.__window = sg.Window("IceFac", size=(640, 360), icon='IceFac.ico').Layout(layout)

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
        codigo = self.input_int("Código do ingrediente = ")
        quantidade = self.input_int("Quantidade do ingrediente = ")
        ingredientes_dict[codigo] = quantidade

    def info(self, sorvete):
        print("---------- Sorvete ----------")
        print("Codigo: ", sorvete.codigo)
        print("Descricao: ", sorvete.sabor)
        print("Quantidade: ", sorvete.quantidade)
        print("Receita:")
        for cod, qtd in sorvete.receita.items():
            print("Código: ", cod)
            print("Quantidade: ", qtd)
            print("--")

    def buscar(self):
        print("---------- Buscar Sorvete ----------")
        codigo = self.input_int("Código do Sorvete a ser encontrado: ")
        return codigo

    def remover(self):
        print("---------- Remover Sorvete ----------")
        codigo = self.input_int("Código do Sorvete a ser removido: ")
        return codigo

    def alterar(self):
        print("---------- Alterar Sorvete ----------")
        codigo = self.input_int("Código do Sorvete a ser alterado: ")
        novo_sabor = input("Novo sabor: ")
        return codigo, novo_sabor

    def produzir(self):
        print("---------- Produzir Sorvete ----------")
        codigo = self.input_int("Código do Sorvete a ser produzido: ")
        quantidade = self.input_int("Quantidade de sorvete a ser produzida: ")
        return codigo, quantidade


"""
    def opcoes(self):
            print("-------- Sorvete ----------")
            print("Escolha a opção: ")
            print("1 - Produzir sorvete")
            print("2 - Adicionar sorvete")
            print("3 - Listar sorvete(s)")
            print("4 - Mostrar sorvete")
            print("5 - Alterar sorvete")
            print("6 - Excluir sorvete")
            print("0 - Retornar ao menu principal")
            opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5, 6])
            return opcao
"""
