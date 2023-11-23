from view.Tela import Tela
import PySimpleGUI as sg


class TelaIngrediente(Tela):
    def __int__(self):
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
            [sg.Text("Ingredientes", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Escolha uma das opções abaixo:",
                    font=("Bahnschrift", 15),
                    text_color="white",
                )
            ],
            [
                sg.Button(
                    "Adicionar Ingrediente",
                    key=1,
                    font=("Bahnschrift", 12),
                    size=(20, 1),
                )
            ],
            [
                sg.Button(
                    "Listar Ingredientes", key=2, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Buscar Ingrediente", key=3, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Alterar Ingrediente", key=4, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Alterar quantidade", key=5, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Excluir Ingrediente", key=6, font=("Bahnschrift", 12), size=(20, 1)
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

    def adicionar(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Novo Ingredidente", font=("Bahnschrift", 21))],
            [
                sg.Text("Nome:", size=(15, 1), font=("Bahnschrift", 15)),
                sg.InputText("", key="nome"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)

        _, values = self.open()
        nome = values["nome"].strip()

        if nome == "":
            tentar_novamente = self.erro_tentar_novamente("Erro: Nome inválido")
            if tentar_novamente.lower() == "no":
                self.close()
                return
            else:
                return self.adicionar()

        sg.Popup("Adicionado com sucesso", text_color="white")
        self.close()
        return nome

    def info(self, ingredientes):
        ings = []
        for ing in ingredientes:
            ings.append(
                [
                    sg.Text("ID: ", text_color="white"),
                    sg.InputText(
                        ing["_Ingrediente__codigo"],
                        use_readonly_for_disable=True,
                        disabled=True,
                        key=f"-id-ing--{ing['_Ingrediente__codigo']}",
                    ),
                ],
            )
            ings.append(
                [
                    sg.Text(
                        f"Nome: {ing['_Ingrediente__nome']}",
                        text_color="white",
                    )
                ],
            )
            ings.append(
                [
                    sg.Text(
                        f"Quantidade: {ing['_Ingrediente__quantidade']}",
                        text_color="white",
                    )
                ],
            )

        ings.append([sg.Button("Ok")])
        info_w = sg.Window("Ingredientes", ings, finalize=True)

        # altera estilo do elemento que contém texto na chave,
        # para parecer elemento de texto comum
        for el in info_w.element_list():
            if el is not None and el.key is not None:
                if "-id-ing--" in el.key:
                    el.Widget.config(readonlybackground=sg.theme_background_color())
                    el.Widget.config(borderwidth=0)

        info_w.Read()
        info_w.close()
        return

    def buscar(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Buscar Ingrediente", font=("Bahnschrift", 21))],
            [
                sg.Text("Nome:", size=(15, 1), font=("Bahnschrift", 12)),
                sg.InputText("", key="nome"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]

        self.__window = sg.Window("IceFac").Layout(layout)

        _, values = self.open()
        nome = values["nome"]
        print(nome)
        self.close()
        return nome

        # print("---------- Buscar Ingrediente ----------")
        # codigo = self.input_int("Código do Ingrediente a ser encontrado: ")
        # return codigo

    def remover(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Excluir Ingrediente", font=("Bahnschrift", 21))],
            [
                sg.Text("Nome:", size=(15, 1), font=("Bahnschrift", 12)),
                sg.InputText("", key="nome"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)
        _, values = self.open()
        nome = values["nome"]
        self.close()
        return nome

    """
        print("---------- Remover Ingrediente ----------")
        codigo = self.input_int("Código do Ingrediente a ser removido: ")
        return codigo
    """

    def alterar(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Alterar Ingrediente", font=("Bahnschrift", 21))],
            [
                sg.Text("Nome:", size=(15, 1), font=("Bahnschrift", 12)),
                sg.InputText("", key="nome"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)
        _, values = self.open()
        nome = values["nome"]
        self.close()
        return nome

        # print("---------- Alterar Ingrediente ----------")
        # codigo = self.input_int("Código do Ingrediente a ser alterado: ")
        # novo_nome = input("Novo nome: ")
        # return codigo, novo_nome

    def alterar_quantidade(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Alterar Quantidade", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Nome do ingrediente para alterar:",
                    size=(15, 1),
                    font=("Bahnschrift", 12),
                ),
                sg.InputText("", key="nome"),
            ],
            [
                sg.Text("Quantidade:", size=(15, 1), font=("Bahnschrift", 12)),
                sg.InputText("", key="quantidade"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac").Layout(layout)
        _, values = self.open()
        nome = values["nome"]
        nova_quantidade = values["quantidade"]
        self.close()
        return nome, nova_quantidade

        # print("---------- Alterar Quantidade de Ingrediente ----------")
        # codigo = self.input_int("Código do Ingrediente a ser alterado: ")
        # nova_quantidade = self.input_int("Nova quantidade: ")
        # return codigo, nova_quantidade

    def erro_tentar_novamente(self, mensagem):
        msg = f"{mensagem}\nDeseja tentar novamente?"

        return sg.Popup(msg, button_type=1)
