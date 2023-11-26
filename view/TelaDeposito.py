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
        if event == 0 or button in (None, "Retornar"):
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
            [sg.Text("Depositos", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Escolha uma das opções abaixo:",
                    font=("Bahnschrift", 15),
                    text_color="white",
                )
            ],
            [
                sg.Button(
                    "Adicionar Depósito", key=1, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Listar Depositos", key=2, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Mostrar Deposito", key=3, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Alterar Deposito", key=4, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Excluir Deposito", key=5, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [sg.Column([[sg.Cancel("Retornar", key=0)]], justification="center")],
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

    # def adicionar(self):
    #     print("---------- Novo Depósito ----------")
    #     descricao = input("Descricao = ")
    #     return descricao
    #
    def adicionar(self, depositos):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Novo Depósito", font=("Bahnschrift", 21))],
            [
                sg.Text("Descrição:", size=(15, 1), font=("Bahnschrift", 15)),
                sg.InputText("", key="descricao"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)

        button, values = self.open()

        if button == "Retornar":
            self.close()
            return

        if values["descricao"] is None:
            return

        descricao = values["descricao"].strip()

        if descricao == "":
            tentar_novamente = self.erro_tentar_novamente("Erro: Descrição inválida")
            if tentar_novamente.lower() == "no":
                self.close()
                return
            else:
                self.close()
                return self.adicionar(depositos)

        for d in depositos:
            if d == descricao:
                tentar_novamente = self.erro_tentar_novamente(
                    "Erro: Descrição já cadastrada"
                )
                if tentar_novamente.lower() == "no":
                    self.close()
                    return
                else:
                    self.close()
                    return self.adicionar(depositos)

        self.close()
        return descricao

    def info(self, depositos):
        deps = []
        deps.append([sg.Text("Depósitos")])
        for dep in depositos:
            deps.append(
                [
                    sg.Text("ID: ", text_color="white"),
                    sg.InputText(
                        dep["_Deposito__codigo"],
                        use_readonly_for_disable=True,
                        disabled=True,
                        key=f"-id-dep--{dep['_Deposito__codigo']}",
                    ),
                ],
            )
            deps.append(
                [
                    sg.Text(
                        f"Descrição: {dep['_Deposito__descricao']}",
                        text_color="white",
                    )
                ],
            )

        if len(depositos) == 0:
            deps.append([sg.Text("Não há depósitos cadastrados")])

        deps.append([sg.Button("Ok")])
        info_w = sg.Window("Depósitos", deps, finalize=True)

        # altera estilo do elemento que contém texto na chave,
        # para parecer elemento de texto comum
        for el in info_w.element_list():
            if el is not None and el.key is not None:
                if "-id-dep--" in el.key:
                    el.Widget.config(readonlybackground=sg.theme_background_color())
                    el.Widget.config(borderwidth=0)

        info_w.Read()
        info_w.close()
        return

    def buscar(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Buscar Depósito", font=("Bahnschrift", 21))],
            [
                sg.Text("Descrição:", size=(15, 1), font=("Bahnschrift", 12)),
                sg.InputText("", key="descricao"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]

        self.__window = sg.Window("IceFac").Layout(layout)

        button, values = self.open()

        self.close()

        if button == "Retornar":
            return

        if values["descricao"] is None or values["descricao"].strip() == "":
            return

        descricao = values["descricao"]
        return descricao

    def remover(self, depositos):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Excluir Depósito", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Selecione o depósito:",
                    size=(15, 1),
                    font=("Bahnschrift", 12),
                ),
            ],
            [
                sg.Combo(
                    depositos,
                    font=("Bahnschrift", 12),
                    key="descricao",
                )
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)
        button, values = self.open()
        self.close()
        if button == "Retornar":
            return

        if values["descricao"] is None or values["descricao"].strip() == "":
            return

        descricao = values["descricao"]
        return descricao

    def alterar(self, depositos):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Alterar Depósito", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Selecione o depósito:",
                    size=(15, 1),
                    font=("Bahnschrift", 12),
                ),
            ],
            [
                sg.Combo(
                    depositos,
                    font=("Bahnschrift", 12),
                    key="deposito",
                )
            ],
            [
                sg.Text("Nova descrição:", size=(15, 1), font=("Bahnschrift", 12)),
                sg.InputText("", key="descricao"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)
        button, values = self.open()

        if button == "Retornar":
            self.close()
            return

        if values["descricao"] is None:
            return

        values["descricao"] = values["descricao"].strip()

        if values["descricao"] == "":
            tentar_novamente = self.erro_tentar_novamente("Erro: Descricao inválida")
            if tentar_novamente.lower() == "no":
                self.close()
                return
            else:
                self.close()
                return self.alterar(depositos)

        self.close()

        if button == "Retornar":
            return

        return values
