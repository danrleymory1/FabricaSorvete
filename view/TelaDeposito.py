from view.Tela import Tela
import PySimpleGUI as sg


class TelaDeposito(Tela):
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
            [sg.Text("Depositos", font=("Bahnschrift", 21))],
            [sg.Text("Escolha uma das opções abaixo:", font=("Bahnschrift", 15), text_color="white")],
            [sg.Button("Adicionar Depósito", key=1, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Listar Depositos", key=2, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Mostrar Deposito", key=3, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Alterar Deposito", key=4, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Button("Excluir Deposito", key=5, font=("Bahnschrift", 12), size=(20, 1))],
            [sg.Column([[sg.Cancel("Retornar", key=0)]], justification='center')]
        ]

        column = sg.Column(layout, justification='center', element_justification='center',
                           vertical_alignment='center')

        # Layout com a coluna centralizada
        layout = [[column]]

        self.__window = sg.Window("IceFac", size=(640, 360), icon='IceFac.ico').Layout(layout)

    def adicionar(self):
        print("---------- Novo Depósito ----------")
        descricao = input("Descricao = ")
        return descricao

    def info(self, deposito):
        print("---------- Depósito ----------")
        print("Codigo: ", deposito.codigo)
        print("Descricao: ", deposito.descricao)

    def buscar(self):
        print("---------- Buscar Depósito ----------")
        codigo = self.input_int("Código do Depósito a ser encontrado: ")
        return codigo

    def remover(self):
        print("---------- Remover Depósito ----------")
        codigo = self.input_int("Código do Depósito a ser removido: ")
        return codigo

    def alterar(self):
        print("---------- Alterar Depósito ----------")
        codigo = self.input_int("Código do Depósito a ser alterado: ")
        nova_descricao = input("Nova descrição: ")
        return codigo, nova_descricao


"""
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
"""