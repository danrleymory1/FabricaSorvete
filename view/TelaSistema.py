from view.Tela import Tela
import PySimpleGUI as sg


class TelaSistema(Tela):
    def __init__(self):
        self.__window = None
        self.init_components()

    def opcoes(self):
        self.init_components()
        values, button = self.__window.Read()
        opcao = 0
        if values == 1:
            opcao = 1
        if values == 2:
            opcao = 2
        if values == 3:
            opcao = 3
        if values == 4:
            opcao = 4
        if values == 0 or button in (None, "Sair"):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Seja bem-vindo!", font=("Bahnschrift", 25))],
            [
                sg.Text(
                    "Escolha uma das opções abaixo:",
                    font=("Bahnschrift", 18),
                    text_color="white",
                )
            ],
            [sg.Button("Sorvete", key=1, font=("Bahnschrift", 15), size=(15, 1))],
            [sg.Button("Ingredientes", key=2, font=("Bahnschrift", 15), size=(15, 1))],
            [
                sg.Button(
                    "Transferencias", key=3, font=("Bahnschrift", 15), size=(15, 1)
                )
            ],
            [sg.Button("Depósitos", key=4, font=("Bahnschrift", 15), size=(15, 1))],
            [sg.Column([[sg.Button("Sair", key=0)]], justification="center")],
        ]

        column = sg.Column(
            layout,
            justification="center",
            element_justification="center",
            vertical_alignment="center",
        )

        # Layout com a coluna centralizada
        layout = [[column]]

        self.__window = sg.Window("IceFac", icon="IceFac.ico").Layout(layout)

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
