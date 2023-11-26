import PySimpleGUI as sg
from view.Tela import Tela


class TelaTransferencia(Tela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def opcoes(self):
        self.init_opcoes()
        values, button = self.__window.Read()
        # opcao = 0
        if values == "1":
            opcao = 1
        if values == "2":
            opcao = 2
        if values == "3":
            opcao = 3
        if values == "0" or button in (None, "Retornar"):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_opcoes(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Transferências", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Escolha uma das opções abaixo:",
                    font=("Bahnschrift", 15),
                    text_color="white",
                )
            ],
            [
                sg.Button(
                    "Transferir produto",
                    key="1",
                    font=("Bahnschrift", 12),
                    size=(20, 1),
                )
            ],
            [
                sg.Button(
                    "Listar Transferências",
                    key="2",
                    font=("Bahnschrift", 12),
                    size=(20, 1),
                )
            ],
            [
                sg.Button(
                    "Mostrar Transferência",
                    key="3",
                    font=("Bahnschrift", 12),
                    size=(20, 1),
                )
            ],
            [sg.Column([[sg.Button("Retornar", key="0")]], justification="center")],
        ]

        column = sg.Column(
            layout,
            justification="center",
            element_justification="center",
            vertical_alignment="center",
        )

        # Layout com a coluna centralizada
        layout = [[column]]

        self.__window = sg.Window("IceFac", size=(640, 360), icon="IceFac.ico").Layout(
            layout
        )

    def adicionar(self):
        print("---------- Nova Transferência  ----------")
        deposito = self.input_int("Depósito de destino = ")
        produtos = {}

        while True:
            self.adicionar_produto(produtos)

            continuar = input("Acrescentar novo produto? [S/N] ")
            if not continuar == "S":
                break

        return deposito, produtos

    def adicionar_produto(self, produtos_dict):
        codigo = self.input_int("Código do produto = ")
        quantidade = self.input_int("Quantidade do produto = ")
        produtos_dict[codigo] = quantidade

    def info(self, transferencia):
        print("---------- Transferência ----------")
        print("Codigo: ", transferencia.codigo)
        print("Código depósito: ", transferencia.deposito_dest.codigo)
        print("Data: ", transferencia.data)
        for cod, qtd in transferencia.produtos.items():
            print("--- Produto ---")
            print("Código: ", cod)
            print("Quantidade: ", qtd)

    def buscar(self):
        print("---------- Buscar Transferência ----------")
        codigo = self.input_int("Código da Transferência a ser encontrada: ")
        return codigo

    def remover(self):
        print("---------- Remover Transferência ----------")
        codigo = self.input_int("Código da Transferência a ser removida: ")
        return codigo

    def alterar(self):
        return
