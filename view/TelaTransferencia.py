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

        self.__window = sg.Window("IceFac", icon="IceFac.ico").Layout(layout)

    def adicionar(self, depositos, sabores):
        sorv_id_dict = {}
        sorv_qtd_dict = {}

        sg.ChangeLookAndFeel("DarkTeal")

        layout = [
            [sg.Text("Nova Transferência")],
            [
                sg.Text("Depósito Destino: "),
                sg.Combo(depositos, key="deposito"),
            ],
            [sg.Text("Produtos: ")],
            [sg.Text("", key="-sorvetes-")],
            [
                sg.Text("Sorvete: "),
                sg.Combo(sabores, key=f"-sorv-"),
                sg.Text("Quantidade: "),
                sg.InputText("", key=f"-qtd-"),
            ],
            [sg.Button("Adicionar Sorvete")],
            [sg.Button("Salvar"), sg.Button("Cancelar")],
        ]

        self.__window = sg.Window("Transferência", layout, resizable=True)

        while True:
            button, values = self.open()
            deposito = values["deposito"]
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

                sorvete_remover = ""
                for k, v in sorv_id_dict.items():
                    if v == target:
                        sorvete_remover = k

                self.__window[target].hide_row()

                sorv_id_dict = {k: v for k, v in sorv_id_dict.items() if v != target}
                sorv_qtd_dict = {
                    k: v for k, v in sorv_qtd_dict.items() if k != sorvete_remover
                }

            elif button == "Salvar":
                sorvete = values["-sorv-"]

                if sorvete is None or sorvete.strip() == "":
                    sg.Popup("Erro: Sorvete inválido\nTente novamente")
                    continue
                if len(sorv_qtd_dict) == 0:
                    sg.Popup("Erro: Não há sorvetes\nAdicione ao menos um sorvete")
                    continue

                self.close()
                return deposito, sorv_qtd_dict

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

    def info(self, transferencias):
        transfs = []
        transfs.append([sg.Text("Transferências")])
        for transf in transferencias:
            transfs.append(
                [
                    sg.Text("ID: ", text_color="white"),
                    sg.InputText(
                        transf["_Transferencia__codigo"],
                        use_readonly_for_disable=True,
                        disabled=True,
                        key=f"-id-transf--{transf['_Transferencia__codigo']}",
                    ),
                ],
            )
            transfs.append(
                [
                    sg.Text(
                        f"Data: {transf['_Transferencia__data']}",
                        text_color="white",
                    )
                ],
            )
            transfs.append(
                [
                    sg.Text(
                        f"Depósito Destino: {transf['_Transferencia__deposito_dest']}",
                        text_color="white",
                    )
                ],
            )
            sorvs = [[sg.Text("Produtos: ")]]
            for sorv in transf["_Transferencia__produtos"]:
                layout = [
                    sg.Text(f"- {sorv['quantidade']} {sorv['sorvete']}"),
                ]

                sorvs.append(layout)

            transfs.append([sg.Column(sorvs)])

        if len(transferencias) == 0:
            transfs.append([sg.Text("Não há transferências realizadas")])

        transfs.append([sg.Button("Ok")])
        info_w = sg.Window("Transferências(s)", transfs, finalize=True)

        # altera estilo do elemento que contém texto na chave,
        # para parecer elemento de texto comum
        for el in info_w.element_list():
            if el is not None and el.key is not None:
                if "-id-transf--" in el.key:
                    el.Widget.config(readonlybackground=sg.theme_background_color())
                    el.Widget.config(borderwidth=0)

        info_w.Read()
        info_w.close()
        return

    def buscar(self):
        sg.ChangeLookAndFeel("DarkTeal")

        layout = [
            [sg.Text("Buscar Transferência(s)", font=("Bahnschrift", 21))],
            [
                sg.Text("Buscar por: "),
                sg.Combo(
                    ["Produto", "Depósito"],
                    key="opcao",
                    enable_events=True,
                ),
                sg.InputText("", key="info"),
            ],
            [
                sg.Button("De", key="data_inicio_button"),
                sg.InputText(
                    "",
                    use_readonly_for_disable=True,
                    disabled=True,
                    key="data_inicio",
                ),
            ],
            [
                sg.Button("Até", key="data_fim_button"),
                sg.InputText(
                    "",
                    use_readonly_for_disable=True,
                    disabled=True,
                    key="data_fim",
                ),
            ],
            [sg.Button("Buscar"), sg.Button("Retornar")],
        ]

        self.__window = sg.Window("IceFac", layout, finalize=True)
        for el in self.__window.element_list():
            if el is not None and el.key is not None:
                if "display" in el.key:
                    el.Widget.config(readonlybackground=sg.theme_background_color())
                    el.Widget.config(borderwidth=0)

        while True:
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

            elif button == "data_inicio_button":
                data_inicio = sg.popup_get_date(close_when_chosen=True)
                if data_inicio:
                    m, d, y = data_inicio
                    self.__window["data_inicio"].update(f"{d}/{m}/{y}")

            elif button == "data_fim_button":
                data_fim = sg.popup_get_date(close_when_chosen=True)
                if data_fim:
                    m, d, y = data_fim
                    self.__window["data_fim"].update(f"{d}/{m}/{y}")

            elif button == "Buscar":
                self.close()
                return values
            elif button in ("Retornar", None):
                self.close()
                return

    def alterar(self):
        pass

    def remover(self):
        pass
