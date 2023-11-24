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
                    "Mostrar Sorvete", key=4, font=("Bahnschrift", 12), size=(20, 1)
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

        self.__window = sg.Window("IceFac", size=(640, 360), icon="IceFac.ico").Layout(
            layout
        )

    def adicionar(self, ingredientes):
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

        self.__window = sg.Window("Ingredientes", layout, resizable=True)

        while True:
            button, values = self.open()

            if button == "Adicionar Ingrediente":
                novo_ing_nome = self.__window["-ing-"].get()
                novo_ing_qtd = self.__window["-qtd-"].get()

                if novo_ing_nome is None or novo_ing_nome.strip() == "":
                    sg.Popup("Erro: Selecione um ingrediente")
                    continue

                if (
                    novo_ing_qtd is None
                    or novo_ing_qtd.strip() == ""
                    or not novo_ing_qtd.isnumeric()
                ):
                    sg.Popup("Erro: Quantidade inválida")
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

                self.__window[target].hide_row()

                ing_id_dict = {k: v for k, v in ing_id_dict.items() if v != target}

            elif button == "Salvar":
                nome = values["nome"]

                if nome is None or nome.strip() == "":
                    sg.Popup("Erro: Nome do sorvete inválido\nTente novamente")
                    continue
                if len(ing_qtd_dict) == 0:
                    sg.Popup(
                        "Erro: Não há ingredientes\nAdicione ao menos um ingrediente"
                    )
                    continue

                return (nome, ing_qtd_dict)

            elif button == "Cancelar":
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
