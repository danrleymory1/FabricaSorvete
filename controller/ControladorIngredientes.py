from exceptions.IngredienteNaoEncontrado import IngredienteNaoEncontrado
from exceptions.IngredienteDiminuirInsuficiente import IngredienteDiminuirInsuficiente
from model.Ingrediente import Ingrediente
from view.TelaIngrediente import TelaIngrediente
from dao.daoIngredientes import IngredienteDAO


class ControladorIngredientes:
    def __init__(self, controlador_sistema):
        self.__ingredientes_dao = IngredienteDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_ingrediente = TelaIngrediente()

    def buscar_ingrediente(self):
        codigo = self.__tela_ingrediente.buscar()

        for ing in self.__ingredientes_dao.get_all():
            if ing.codigo == codigo:
                self.__tela_ingrediente.info([ing.__dict__])
                return

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def buscar_por_nome(self):
        nome = self.__tela_ingrediente.buscar()

        res = []

        for ing in self.__ingredientes_dao.get_all():
            if nome.upper() in ing.nome.upper():
                res.append(ing.__dict__)

        if len(res) == 0:
            self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")
        else:
            self.__tela_ingrediente.info(res)

    def adicionar_ingrediente(self):
        nome = self.__tela_ingrediente.adicionar()

        if nome == "":
            return

        novo_ingrediente = Ingrediente(str(nome))

        self.__ingredientes_dao.add(novo_ingrediente)

        self.__tela_ingrediente.mensagem_sucesso("Ingrediente adicionado com sucesso")

    def remover_ingrediente(self):
        codigo = self.__tela_ingrediente.remover()

        for ing in self.__ingredientes_dao.get_all():
            if ing.codigo == codigo:
                self.__ingredientes_dao.remove(ing.codigo)
                self.__tela_ingrediente.mensagem_sucesso(
                    "Ingrediente removido com sucesso"
                )
                return

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def alterar_ingrediente(self):
        (codigo, novo_nome) = self.__tela_ingrediente.alterar()

        for i, ing in enumerate(self.__ingredientes_dao.get_all()):
            if ing.codigo == codigo:
                self.__ingredientes_dao.update(novo_nome)
                self.__tela_ingrediente.mensagem_sucesso(
                    "Ingrediente alterado com sucesso"
                )
                return

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar_ingrediente,
            2: self.listar_ingredientes,
            3: self.buscar_por_nome,
            4: self.alterar_ingrediente,
            5: self.alterar_quantidade,
            6: self.remover_ingrediente,
            0: self.retornar,
        }
        while True:
            lista_opcoes[self.__tela_ingrediente.opcoes()]()

    def buscar_por_codigo(self, codigo):
        for ing in self.__ingredientes_dao.get_all():
            if ing.codigo == codigo:
                return ing
        return None

    def acrescentar_quantidade(self, codigo, quantidade):
        for ing in self.__ingredientes_dao.get_all():
            if codigo == ing.codigo:
                ing.quantidade = ing.quantidade + quantidade
                self.__ingredientes_dao.update(ing.quantidade)
                return
        raise IngredienteNaoEncontrado(codigo)

    def diminuir_quantidade(self, codigo, quantidade):
        for ing in self.__ingredientes_dao.get_all():
            if codigo == ing.codigo:
                nova_quantidade = ing.quantidade - quantidade
                if nova_quantidade < 0:
                    raise IngredienteDiminuirInsuficiente(ing.nome, ing.quantidade)
                ing.quantidade = nova_quantidade
                return
        raise IngredienteNaoEncontrado(codigo)

    def listar_ingredientes(self):
        dict_list = []

        for ing in self.__ingredientes_dao.get_all():
            dict_list.append(ing.__dict__)

        self.__tela_ingrediente.info(dict_list)

    def alterar_quantidade(self):
        ingredientes = [
            i.__dict__["_Ingrediente__nome"] for i in self.__ingredientes_dao.get_all()
        ]

        values = self.__tela_ingrediente.alterar_quantidade(ingredientes)
        nome = values["nome"]
        quantidade = values["quantidade"]

        try:
            for ing in self.__ingredientes_dao.get_all():
                if ing.nome == nome:
                    ing.quantidade = quantidade
                    self.__ingredientes_dao.update(ing)
                    self.__tela_ingrediente.mensagem_sucesso(
                        "Quantidade alterada com sucesso"
                    )
                    return
            raise IngredienteNaoEncontrado(nome)

        except Exception as e:
            self.__tela_ingrediente.mensagem_erro(e)
