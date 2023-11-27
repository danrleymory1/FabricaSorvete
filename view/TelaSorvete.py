from view.Tela import Tela
import PySimpleGUI as sg
import uuid


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
            [sg.Text("Sorvete", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Escolha uma das opções abaixo:",
                    font=("Bahnschrift", 15),
                    text_color="white",
                )
            ],
            [
                sg.Button(
                    "Produzir Sorvete", key=1, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Adicionar Sorvete", key=2, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Listar Sorvete(s)", key=3, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Buscar Sorvete", key=4, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Alterar Sorvete", key=5, font=("Bahnschrift", 12), size=(20, 1)
                )
            ],
            [
                sg.Button(
                    "Excluir Sorvete", key=6, font=("Bahnschrift", 12), size=(20, 1)
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

        self.__window = sg.Window("IceFac - Sorvetes", icon="IceFac.ico").Layout(layout)

    def adicionar(self, ingredientes, sorvetes):
        ing_id_dict = {}
        ing_qtd_dict = {}

        sg.ChangeLookAndFeel("DarkTeal")

        layout = [
            [sg.Text("Nome do Sorvete: "), sg.InputText("", key="nome")],
            [sg.Text("Ingredientes")],
            [sg.Text("", key="-ingredientes-")],
            [
                sg.Text("Ingrediente: "),
                sg.Combo(ingredientes, key=f"-ing-"),
                sg.Text("Quantidade: "),
                sg.InputText("", key=f"-qtd-"),
            ],
            [sg.Button("Adicionar Ingrediente")],
            [sg.Button("Salvar"), sg.Button("Cancelar")],
        ]

        self.__window = sg.Window("IceFac - Sorvetes", layout, resizable=True)

        while True:
            button, values = self.open()

            if button == "Adicionar Ingrediente":
                novo_ing_nome = self.__window["-ing-"].get()
                novo_ing_qtd = self.__window["-qtd-"].get()

                if novo_ing_nome is None or novo_ing_nome.strip() == "":
                    sg.Popup("Selecione um ingrediente")
                    continue

                if (
                    novo_ing_qtd is None
                    or novo_ing_qtd.strip() == ""
                    or not novo_ing_qtd.isnumeric()
                ):
                    sg.Popup("Quantidade inválida")
                    continue

                if novo_ing_nome in ing_id_dict.keys():
                    button = sg.Popup(
                        "Ingrediente já selecionado!\nAlterar quantidade?",
                        button_type=1,
                    )

                    if button == "No":
                        continue
                    else:
                        target = ing_id_dict[novo_ing_nome]
                        self.__window[target].hide_row()

                novo_ing_elemento, novo_ing_id = self.novo_ingrediente(
                    novo_ing_nome, novo_ing_qtd
                )

                ing_id_dict[novo_ing_nome] = novo_ing_id
                ing_qtd_dict[novo_ing_nome] = int(novo_ing_qtd)

                self.__window.extend_layout(
                    self.__window["-ingredientes-"], novo_ing_elemento
                )
                self.__window.refresh()

            elif "-remover-" in button:
                target = button.replace("-remover-", "")

                nome_remover = ""
                for k, v in ing_id_dict.items():
                    if v == target:
                        nome_remover = k

                self.__window[target].hide_row()

                ing_id_dict = {k: v for k, v in ing_id_dict.items() if v != target}
                ing_qtd_dict = {
                    k: v for k, v in ing_qtd_dict.items() if k != nome_remover
                }

            elif button == "Salvar":
                nome = values["nome"]

                if nome is None or nome.strip() == "":
                    sg.Popup("Nome do sorvete inválido\nTente novamente")
                    continue
                if nome.upper() in sorvetes:
                    sg.Popup("Sabor já cadastrado no sistema\nTente novamente")
                    continue
                if len(ing_qtd_dict) == 0:
                    sg.Popup("Não há ingredientes\nAdicione ao menos um ingrediente")
                    continue

                self.close()
                return nome, ing_qtd_dict

            elif button in ("Cancelar", None):
                self.close()
                return None

    def novo_ingrediente(self, nome, qtd):
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

    def info(self, sorvetes_receitas):
        sorvs = []
        sorvs.append([sg.Text("Sorvetes")])
        for sorv in sorvetes_receitas:
            sorvs.append(
                [
                    sg.Text("ID: ", text_color="white"),
                    sg.InputText(
                        sorv["_Sorvete__codigo"],
                        use_readonly_for_disable=True,
                        disabled=True,
                        key=f"-id-sorv--{sorv['_Sorvete__codigo']}",
                    ),
                ],
            )
            sorvs.append(
                [
                    sg.Text(
                        f"Sabor: {sorv['_Sorvete__sabor']}",
                        text_color="white",
                    )
                ],
            )
            sorvs.append(
                [
                    sg.Text(
                        f"Quantidade: {sorv['_Sorvete__quantidade']}",
                        text_color="white",
                    )
                ],
            )

            ings = [[sg.Text("Receita: ")]]
            for ing in sorv["_Sorvete__receita"]:
                layout = [
                    sg.Text(
                        f"- {ing['quantidade']} {ing['ingrediente']['_Ingrediente__nome']}"
                    ),
                ]

                ings.append(layout)

            sorvs.append([sg.Column(ings)])

        if len(sorvetes_receitas) == 0:
            sorvs.append([sg.Text("Não há ingredientes cadastrados")])

        sorvs.append([sg.Button("Ok")])
        info_w = sg.Window("IceFac - Sorvetes", sorvs, finalize=True)

        # altera estilo do elemento que contém texto na chave,
        # para parecer elemento de texto comum
        for el in info_w.element_list():
            if el is not None and el.key is not None:
                if "-id-sorv--" in el.key:
                    el.Widget.config(readonlybackground=sg.theme_background_color())
                    el.Widget.config(borderwidth=0)

        info_w.Read()
        info_w.close()
        return

    def buscar(self):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Buscar Sorvete", font=("Bahnschrift", 21))],
            [
                sg.Text("Buscar por: "),
                sg.Combo(["Sabor", "Ingrediente"], key="opcao"),
                sg.InputText("", key="info"),
            ],
            [sg.Button("Buscar"), sg.Button("Retornar")],
        ]

        self.__window = sg.Window("IceFac - Sorvetes").Layout(layout)

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

    def remover(self, sorvetes):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Excluir Sorvete", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Selecione o sorvete:",
                    font=("Bahnschrift", 12),
                ),
            ],
            [
                sg.Combo(
                    sorvetes,
                    font=("Bahnschrift", 12),
                    key="sabor",
                )
            ],
            [sg.Button("Confirmar"), sg.Button("Cancelar")],
        ]
        self.__window = sg.Window("IceFac - Sorvetes").Layout(layout)
        button, values = self.open()
        self.close()

        if button in ("Cancelar", None):
            return

        sabor = values["sabor"]
        if sabor is None or sabor.strip() == "":
            tentar_novamente = self.erro_tentar_novamente("Nenhum sabor selecionado")
            if tentar_novamente.lower() == "no":
                self.close()
                return
            else:
                self.close()
                return self.remover(sorvetes)

        return sabor

    def alterar(self, sorvetes):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Alterar Sorvete", font=("Bahnschrift", 21))],
            [sg.Text("Selecione o sorvete a alterar:")],
            [sg.Combo(sorvetes, key="sorvete")],
            [sg.Text("Novo Nome:"), sg.InputText(default_text="", key="novo_sabor")],
            [sg.Button("Alterar"), sg.Button("Cancelar")],
        ]
        self.__window = sg.Window("IceFac - Sorvetes").Layout(layout)

        button, values = self.open()
        if button in ("Cancelar", None):
            self.close()
            return

        values["novo_sabor"] = values["novo_sabor"].strip()

        if values["novo_sabor"] == "":
            tentar_novamente = self.erro_tentar_novamente("Nome inválido")
            if tentar_novamente.lower() == "no":
                self.close()
                return
            else:
                self.close()
                return self.alterar(sorvetes)
        if values["novo_sabor"].upper() in [s.upper() for s in sorvetes]:
            tentar_novamente = self.erro_tentar_novamente(
                "Sabor já inserido no sistema"
            )
            if tentar_novamente.lower() == "no":
                self.close()
                return
            else:
                self.close()
                return self.alterar(sorvetes)

        self.close()
        return values

    def produzir(self, sabores):
        sg.ChangeLookAndFeel("DarkTeal")
        layout = [
            [sg.Text("Produzir", font=("Bahnschrift", 21))],
            [
                sg.Text(
                    "Selecione o sabor:",
                    size=(15, 1),
                    font=("Bahnschrift", 12),
                ),
            ],
            [
                sg.Combo(
                    sabores,
                    font=("Bahnschrift", 12),
                    key="sabor",
                )
            ],
            [
                sg.Text("Quantidade:", size=(15, 1), font=("Bahnschrift", 12)),
                sg.InputText("", key="quantidade"),
            ],
            [sg.Button("Confirmar"), sg.Button("Retornar")],
        ]
        self.__window = sg.Window("IceFac - Sorvetes").Layout(layout)
        button, values = self.open()

        self.close()

        if button in ("Retornar", None):
            return

        if button == "Confirmar" and (
            values["quantidade"] is None
            or values["quantidade"].strip() == ""
            or not values["quantidade"].strip().isnumeric()
        ):
            res = self.erro_tentar_novamente("Quantidade inválida")
            if res == "No":
                return
            else:
                return self.produzir(sabores)
        elif button == "Confirmar" and (
            values["sabor"] is None or values["sabor"].strip() == ""
        ):
            res = self.erro_tentar_novamente("Selecione um sabor")
        return values
