from view.Tela import Tela
import PySimpleGUI as sg


class TelaSistema(Tela):
    def __init__(self):
        self.__window = None
        self.init_components()
    
    def opcoes(self):
        event, values = self.__window.Read()
        opcao = 0
        if event == 1:
            opcao = 1
        if event == 2:
            opcao = 2
        if event == 3:
            opcao = 3
        if event == 4:
            opcao = 4
        if event == 0 or None:
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal')
        layout = [
            [sg.Text("Seja bem-vindo!", font=("Bahnschrift", 25))],
            [sg.Text("Escolha uma das opções abaixo:", font=("Bahnschrift", 18), text_color="white")],
            [sg.Button("Sorvete", key=1, font=("Bahnschrift", 15), size=(15, 1))],
            [sg.Button("Ingredientes",  key=2, font=("Bahnschrift", 15), size=(15, 1))],
            [sg.Button("Transferencias", key=3, font=("Bahnschrift", 15), size=(15, 1))],
            [sg.Button("Depositos", key=4, font=("Bahnschrift", 15), size=(15, 1))],
            [sg.Column([[sg.Button("Sair", key=0)]], justification='center')]
        ]

        column = sg.Column(layout, justification='center', element_justification='center',
                           vertical_alignment='center')

        # Layout com a coluna centralizada
        layout = [[column]]

        self.__window = sg.Window("IceFac", size=(640, 360), icon='IceFac.ico').Layout(layout)

    def buscar(self):
        return

    def info(self, objeto):
        return

    def adicionar(self):
        return

    def remover(self):
        return

    def alterar(self):
        return
"""
    def opcoes(self):
        super().limpar_tela()
        print("---------- IceFac ----------")
        print("Escolha uma das opções abaixo: ")
        print("1 - Sorvete")
        print("2 - Ingrediente")
        print("3 - Transferencia")
        print("4 - Deposito")
        print("0 - Finalizar")
        opcao = super().opcao_input("Opção = ", [0, 1, 2, 3, 4, 5])
        return opcao
"""