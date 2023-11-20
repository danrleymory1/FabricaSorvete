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
                self.__tela_ingrediente.info(ing.__dict__)
                return

        self.__tela_ingrediente.mensagem_erro("Ingrediente não encontrado")

    def adicionar_ingrediente(self):
        nome = self.__tela_ingrediente.adicionar()

        novo_ingrediente = Ingrediente(nome["nome"])

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
            3: self.buscar_ingrediente,
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
        self.__tela_ingrediente.mensagem("--- Ingredientes ---")
        self.__tela_ingrediente.info(self.__ingredientes_dao.get_all())

    def alterar_quantidade(self):
        (codigo, quantidade) = self.__tela_ingrediente.alterar_quantidade()

        try:
            for ing in self.__ingredientes_dao.get_all():
                if ing.codigo == codigo:
                    ing.quantidade = quantidade
                    self.__ingredientes_dao.update(ing.codigo)
                    self.__tela_ingrediente.mensagem_sucesso(
                        "Quantidade alterada com sucesso"
                    )
                    return
            raise IngredienteNaoEncontrado(codigo)

        except Exception as e:
            self.__tela_ingrediente.mensagem_erro(e)
