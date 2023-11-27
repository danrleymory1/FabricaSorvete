from exceptions.SorveteInsuficiente import SorveteInsuficiente
from exceptions.ReceitaInvalida import ReceitaInvalida
from exceptions.SorveteNaoEncontrado import SorveteNaoEncontrado
from model.Sorvete import Sorvete
from dao.daoSorvetes import SorveteDAO
from view.TelaSorvete import TelaSorvete
import copy


class ControladorSorvetes:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_sistema = controlador_sistema
        self.__tela_sorvetes = TelaSorvete()
        self.__sorvetes_dao = SorveteDAO()

    @property
    def sorvetes_dao(self):
        return self.__sorvetes_dao

    def buscar_sorvete(self):
        val = self.__tela_sorvetes.buscar()
        if val is None:
            return

        opcao = val["opcao"]
        info = val["info"]

        res = []
        if opcao == "Sabor":
            for sorv in self.__sorvetes_dao.get_all():
                if info.upper() in sorv.sabor.upper():
                    res.append(sorv)

        elif opcao == "Ingrediente":
            for sorv in self.__sorvetes_dao.get_all():
                for ing in sorv.receita:
                    if info.upper() in ing["ingrediente"].nome.upper():
                        res.append(sorv)

        if len(res) == 0:
            self.__tela_sorvetes.mensagem_erro("Sorvete não encontrado")

        sorvetes_para_tela = self.preparar_para_tela(res)
        self.__tela_sorvetes.info(sorvetes_para_tela)

    def adicionar_sorvete(self):
        ingredientes = (
            self.__controlador_sistema.controlador_ingredientes.ingredientes_dao.get_all()
        )

        ingredientes_dict = [i.__dict__["_Ingrediente__nome"] for i in ingredientes]

        sorvetes = [s.sabor.upper() for s in self.__sorvetes_dao.get_all()]

        val = self.__tela_sorvetes.adicionar(ingredientes_dict, sorvetes)
        if val is None:
            return

        sabor, ingredientes_receita = val

        receita = []

        found = False
        for ingrediente in ingredientes:
            for novo_ing in ingredientes_receita.keys():
                if ingrediente.nome == novo_ing:
                    d = {}
                    d["ingrediente"] = ingrediente
                    d["quantidade"] = ingredientes_receita[novo_ing]

                    receita.append(d)
                    found = True
                    break

        if not found:
            self.__tela_sorvetes.mensagem_erro("Erro: Ingrediente não encontrado")

        novo_sorvete = Sorvete(sabor, receita)

        self.__sorvetes_dao.add(novo_sorvete)
        self.__tela_sorvetes.mensagem_sucesso("Sorvete adicionado com sucesso")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.produzir_sorvete,
            2: self.adicionar_sorvete,
            3: self.listar_sorvetes,
            4: self.buscar_sorvete,
            5: self.alterar_sorvete,
            6: self.remover_sorvete,
            0: self.retornar,
        }
        while True:
            lista_opcoes[self.__tela_sorvetes.opcoes()]()

    def validar_ingrediente_quantidade(self, ingrediente, qtd):
        if qtd < 1:
            raise ReceitaInvalida(ingrediente, qtd)
        for ing in self.__controlador_sistema.controlador_ingredientes.ingredientes:
            if ing.codigo == ingrediente.codigo and ingrediente.quantidade >= qtd:
                return True
        raise ReceitaInvalida(ingrediente, qtd)

    def produzir_sorvete(self):
        sorvetes = self.__sorvetes_dao.get_all()

        sabores = [s.sabor for s in sorvetes]

        if sorvetes is None:
            return

        val = self.__tela_sorvetes.produzir(sabores)
        if val is None:
            return

        sabor = val["sabor"]
        quantidade = int(val["quantidade"])

        ings_to_update = []
        ings_bkp = []

        try:
            for sorv in sorvetes:
                if sorv.sabor == sabor:
                    for ing in sorv.receita:
                        ingrediente = self.__controlador_sistema.controlador_ingredientes.ingredientes_dao.get(
                            ing["ingrediente"].codigo
                        )

                        ings_to_update.append(ingrediente)
                        ings_bkp.append(copy.copy(ingrediente))

                        self.__controlador_sistema.controlador_ingredientes.diminuir_quantidade(
                            ingrediente, ing["quantidade"] * quantidade
                        )

                    sorv.quantidade = sorv.quantidade + quantidade

                    self.__sorvetes_dao.update(sorv)

                    for ing in ings_to_update:
                        self.__controlador_sistema.controlador_ingredientes.ingredientes_dao.update(
                            ing
                        )

        except Exception as e:
            ingredientes = (
                self.__controlador_sistema.controlador_ingredientes.ingredientes_dao.get_all()
            )
            for bkp in ings_bkp:
                for ing in ingredientes:
                    if ing.codigo == bkp.codigo:
                        ing.quantidade = bkp.quantidade
                        self.__controlador_sistema.controlador_ingredientes.ingredientes_dao.update(
                            ing
                        )
            self.__tela_sorvetes.mensagem_erro(e)

    def listar_sorvetes(self):
        sorvetes = self.__sorvetes_dao.get_all()

        sorvetes_para_tela = self.preparar_para_tela(sorvetes)
        self.__tela_sorvetes.info(sorvetes_para_tela)

    def alterar_sorvete(self):
        sorvetes = self.__sorvetes_dao.get_all()
        sorvetes_string = [s.sabor for s in sorvetes]

        values = self.__tela_sorvetes.alterar(sorvetes_string)
        if values is None:
            return

        sabor = values["sorvete"]
        novo_sabor = values["novo_sabor"]

        try:
            for sorv in sorvetes:
                if sorv.sabor == sabor:
                    sorv.sabor = novo_sabor
                    self.__sorvetes_dao.update(sorv)
                    self.__tela_sorvetes.mensagem_sucesso(
                        "Sorvete alterado com sucesso"
                    )
                    return

            raise SorveteNaoEncontrado(sabor)

        except Exception as e:
            self.__tela_sorvetes.mensagem_erro(e)

    def remover_sorvete(self):
        sorvetes = self.__sorvetes_dao.get_all()
        sorvetes_string = [s.sabor for s in sorvetes]

        sabor = self.__tela_sorvetes.remover(sorvetes_string)
        if sabor is None:
            return

        try:
            for sorv in sorvetes:
                if sorv.sabor == sabor:
                    self.__sorvetes_dao.remove(sorv)
                    self.__tela_sorvetes.mensagem_sucesso(
                        "Sorvete removido com sucesso"
                    )
                    return

            raise SorveteNaoEncontrado(sabor)

        except Exception as e:
            self.__tela_sorvetes.mensagem_erro(e)

    def diminuir_quantidade(self, sabor, quantidade):
        sorvetes = self.__sorvetes_dao.get_all()

        try:
            for sorv in sorvetes:
                if sorv.sabor == sabor:
                    nova_quantidade = sorv.quantidade - quantidade
                    if nova_quantidade < 0:
                        raise SorveteInsuficiente(
                            sorv.sabor, quantidade, sorv.quantidade
                        )

                    sorv.quantidade = nova_quantidade
            raise SorveteNaoEncontrado(sabor)
        except Exception as e:
            return e

    def preparar_para_tela(self, sorvetes):
        sorvetes_receitas = []

        for sorv in sorvetes:
            ingredientes = []

            for ing in sorv.receita:
                receita_item_dict = {
                    "quantidade": ing["quantidade"],
                    "ingrediente": ing["ingrediente"].__dict__.copy(),
                }

                ingredientes.append(receita_item_dict)

            sorvete_dict = sorv.__dict__.copy()

            sorvete_dict["_Sorvete__receita"] = ingredientes
            sorvetes_receitas.append(sorvete_dict)

        return sorvetes_receitas
