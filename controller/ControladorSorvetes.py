from exceptions.ReceitaInvalida import ReceitaInvalida
from exceptions.SorveteNaoEncontrado import SorveteNaoEncontrado
from model.Sorvete import Sorvete
from view.TelaSorvete import TelaSorvete


class ControladorSorvetes:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_sorvetes = TelaSorvete()
        self.__sorvetes = []

    def buscar_sorvete(self):
        codigo = self.__tela_sorvetes.buscar()

        for sorv in self.__sorvetes:
            if sorv.codigo == codigo:
                self.__tela_sorvetes.info(sorv)
                return

        self.__tela_sorvetes.mensagem_erro("Sabor não encontrado")

    def adicionar_sorvete(self):
        (sabor, receita) = self.__tela_sorvetes.adicionar()

        novo_sorvete = Sorvete(sabor, receita)

        for cod, qtd in receita.items():
            try:
                self.validar_ingrediente_quantidade(cod, qtd)
            except Exception as e:
                self.__tela_sorvetes.mensagem_erro(e)

        self.__sorvetes.append(novo_sorvete)

        self.__tela_sorvetes.mensagem_sucesso("Sabor adicionado com sucesso")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.produzir_sorvete(),
            2: self.adicionar_sorvete(),
            3: self.listar_sorvetes(),
            4: self.buscar_sorvete(),
            5: self.alterar_sorvete(),
            6: self.remover_sorvete(),
        }
        while True:
            lista_opcoes[self.__tela_sorvetes.opcoes()]()

    def validar_ingrediente_quantidade(self, cod, qtd):
        if qtd < 1:
            raise ReceitaInvalida(cod, qtd)
        for ing in self.__controlador_sistema.controlador_ingredientes.ingredientes:
            if ing.codigo == cod:
                return True
        raise ReceitaInvalida(cod, qtd)

    def produzir_sorvete(self):
        (codigo, quantidade) = self.__tela_sorvetes.produzir()

        try:
            self.__controlador_sistema.controlador_ingredientes.diminuir_quantidade(
                codigo, quantidade
            )

            for sorv in self.__sorvetes:
                if sorv.codigo == codigo:
                    sorv.quantidade += quantidade
                    return True
            raise SorveteNaoEncontrado(codigo)

        except Exception as e:
            self.__tela_sorvetes.mensagem_erro(e)

    def listar_sorvetes(self):
        self.__tela_sorvetes.mensagem("---- Sorvetes ----")
        for sorv in self.__sorvetes:
            self.__tela_sorvetes.info(sorv)

    def alterar_sorvete(self):
        (codigo, novo_sabor) = self.__tela_sorvetes.alterar()

        try:
            for sorv in self.__sorvetes:
                if sorv.codigo == codigo:
                    sorv.sabor = novo_sabor
                    return True
            raise SorveteNaoEncontrado(codigo)

        except Exception as e:
            self.__tela_sorvetes.mensagem_erro(e)

    def remover_sorvete(self):
        codigo = self.__tela_sorvetes.remover()

        try:
            for sorv in self.__sorvetes:
                if sorv.codigo == codigo:
                    self.__sorvetes.remove(sorv)
                    return True
            raise SorveteNaoEncontrado(codigo)

        except Exception as e:
            self.__tela_sorvetes.mensagem_erro(e)

    def buscar_por_codigo(self, codigo):
        for ing in self.__sorvetes:
            if ing.codigo == codigo:
                return ing
        return None
