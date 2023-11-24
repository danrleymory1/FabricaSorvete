from exceptions.SorveteInsuficiente import SorveteInsuficiente
from exceptions.ReceitaInvalida import ReceitaInvalida
from exceptions.SorveteNaoEncontrado import SorveteNaoEncontrado
from model.Receita import Receita
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
        self.__tela_sorvetes.adicionar()

    # (sabor, receita) = self.__tela_sorvetes.adicionar()

    # try:
    #     r = Receita()
    #     for cod, qtd in receita.items():
    #         ingrediente = self.__controlador_sistema.controlador_ingredientes.buscar_por_codigo(
    #             cod
    #         )
    #         self.validar_ingrediente_quantidade(ingrediente, qtd)
    #         r.adicionar_ingrediente_e_quantidade(ingrediente, qtd)
    #         # colocar método na classe sorvete

    #     novo_sorvete = Sorvete(sabor, r)
    #     self.__sorvetes.append(novo_sorvete)
    #     self.__tela_sorvetes.mensagem_sucesso("Sabor adicionado com sucesso")
    # except Exception as e:
    #     self.__tela_sorvetes.mensagem_erro(e)

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
        (codigo, quantidade) = self.__tela_sorvetes.produzir()

        try:
            sorvete = self.buscar_por_codigo(codigo)

            if sorvete == None:
                raise SorveteNaoEncontrado(codigo)

            for cod, qtd in sorvete.receita.items():
                self.__controlador_sistema.controlador_ingredientes.diminuir_quantidade(
                    cod, qtd * quantidade
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

    def diminuir_quantidade(self, codigo, quantidade):
        sorvete = self.buscar_por_codigo(codigo)
        if sorvete == None:
            raise SorveteNaoEncontrado(codigo)

        nova_quantidade = sorvete.quantidade - quantidade
        if nova_quantidade < 0:
            raise SorveteInsuficiente(sorvete.sabor, quantidade, sorvete.quantidade)

        sorvete.quantidade = nova_quantidade
