import PySimpleGUI as sg
from view.Tela import Tela
import uuid


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

    def open(self):
        event, button = self.__window.Read()
        return event, button

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

    def adicionar(self, sorvetes):
        sorv_id_dict = {}
        sorv_qtd_dict = {}

        sg.ChangeLookAndFeel("DarkTeal")

        layout = [
            [sg.Text("Nova Transferência")],
            [sg.Text("Produtos: ")],
            [sg.Text("", key="-sorvetes-")],
            [
                sg.Text("Sorvete: "),
                sg.Combo(sorvetes, key=f"-sorv-"),
                sg.Text("Quantidade: "),
                sg.InputText("", key=f"-qtd-"),
            ],
            [sg.Button("Adicionar Sorvete")],
            [sg.Button("Salvar"), sg.Button("Cancelar")],
        ]

        self.__window = sg.Window("Transferência", layout, resizable=True)

        while True:
            button, values = self.open()

            if button == "Adicionar Sorvete":
                novo_sorv_sabor = self.__window["-sorv-"].get()
                novo_sorv_qtd = self.__window["-qtd-"].get()

                if novo_sorv_sabor is None or novo_sorv_sabor.strip() == "":
                    sg.Popup("Erro: Selecione um sorvete")
                    continue

                if (
                        novo_sorv_qtd is None
                        or novo_sorv_qtd.strip() == ""
                        or not novo_sorv_qtd.isnumeric()
                ):
                    sg.Popup("Erro: Quantidade inválida")
                    continue

                if novo_sorv_sabor in sorv_id_dict.keys():
                    button = sg.Popup(
                        "Sorvete já selecionado!\nAlterar quantidade?",
                        button_type=1,
                    )

                    if button == "No":
                        continue
                    else:
                        target = sorv_id_dict[novo_sorv_sabor]
                        self.__window[target].hide_row()

                novo_sorv_elemento, novo_sorv_id = self.novo_sorvete(
                    novo_sorv_sabor, novo_sorv_qtd
                )

                sorv_id_dict[novo_sorv_sabor] = novo_sorv_id
                sorv_qtd_dict[novo_sorv_sabor] = int(novo_sorv_qtd)

                self.__window.extend_layout(
                    self.__window["-sorvetes-"], novo_sorv_elemento
                )
                self.__window.refresh()

            elif "-remover-" in button:
                target = button.replace("-remover-", "")

                self.__window[target].hide_row()

                sorv_id_dict = {k: v for k, v in sorv_id_dict.items() if v != target}

            elif button == "Salvar":
                sabor = values["sabor"]

                if sabor is None or sabor.strip() == "":
                    sg.Popup("Erro: sabor do sorvete inválido\nTente novamente")
                    continue
                if len(sorv_qtd_dict) == 0:
                    sg.Popup(
                        "Erro: Não há sorvetes\nAdicione ao menos um sorvete"
                    )
                    continue

                self.close()
                return sabor, sorv_qtd_dict

            elif button == "Cancelar":
                self.close()
                return None

    def novo_sorvete(self, nome, qtd):
        id = str(uuid.uuid4())

        return (
            [
                [
                    sg.Text(f"{qtd}\t{nome}", key=f"{id}"),
                    sg.Button("Remover", key=f"-remover-{id}"),
                ]
            ],
            id,
        )

    """    
        print("---------- Nova Transferência  ----------")
        deposito = self.input_int("Depósito de destino = ")
        produtos = {}

        while True:
            self.adicionar_produto(produtos)

            continuar = input("Acrescentar novo produto? [S/N] ")
            if not continuar == "S":
                break

        return deposito, produtos
    """

    """ 
    def adicionar_produto(self, produtos_dict):
        codigo = self.input_int("Código do produto = ")
        quantidade = self.input_int("Quantidade do produto = ")
        produtos_dict[codigo] = quantidade
    """

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
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Buscar Transferência(s)", font=("Bahnschrift", 21))],
            [
                sg.Text("Buscar por: "),
                sg.Combo(["Produto", "Data"], key="opcao"),
                sg.InputText("", key="info"),
            ],
            [sg.Button("Buscar"), sg.Button("Retornar")],
        ]

        self.__window = sg.Window("IceFac").Layout(layout)

        button, values = self.open()

        if button == "Buscar" and (
                (values["info"] is None or values["info"].strip() == "")
                or (values["opcao"] is None or values["opcao"].strip() == "")
        ):
            res = self.erro_tentar_novamente("Pesquisa inválida.")
            if res == "No":
                self.close()
                return
            else:
                self.close()
                return self.buscar()

        self.close()

        if button in ("Retornar", None):
            return

        return values

    """
        print("---------- Buscar Transferência ----------")
        codigo = self.input_int("Código da Transferência a ser encontrada: ")
        return codigo
    """

    def remover(self, transferencias):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Excluir Transferência", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Selecione a Transferência:",
                    font=("Bahnschrift", 12),
                ),
            ],
            [
                sg.Combo(
                    transferencias,
                    font=("Bahnschrift", 12),
                    key="transferencia",
                )
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)
        button, values = self.open()
        self.close()

        if button in ("Cancelar", None):
            return

        transferencia = values["transferencia"]
        if transferencia is None or transferencia.strip() == "":
            tentar_novamente = self.erro_tentar_novamente("Nenhuma transferência selecionada")
            if tentar_novamente.lower() == "no":
                self.close()
                return
            else:
                self.close()
                return self.remover(transferencias)

        return transferencia

    """
        print("---------- Remover Transferência ----------")
        codigo = self.input_int("Código da Transferência a ser removida: ")
        return codigo
    """

    def alterar(self, value):
        return
