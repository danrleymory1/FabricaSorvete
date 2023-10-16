from exceptions.DepositoNaoEncontrado import DepositoNaoEncontrado
from exceptions.SorveteNaoEncontrado import SorveteNaoEncontrado
from exceptions.TransferenciaNaoEncontrada import TransferenciaNaoEncontrada
from view.TelaTransferencia import TelaTransferencia
from model.Transferencia import Transferencia


class ControladorTransferencias:
    def __init__(self, controlador_sistema):
        self.__transferencias = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_transferencia = TelaTransferencia()

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def nova_transferencia(self):
        (codigo, produtos) = self.__tela_transferencia.adicionar()

        deposito = None
        try:
            for dep in self.__controlador_sistema.controlador_depositos.depositos:
                if dep.codigo == codigo:
                    deposito = dep

            if deposito == None:
                raise DepositoNaoEncontrado(codigo)

            for cod, qtd in produtos.items():
                sorvete = (
                    self.__controlador_sistema.controlador_sorvetes.buscar_por_codigo(
                        cod
                    )
                )
                if sorvete == None:
                    raise SorveteNaoEncontrado(cod)

                self.__controlador_sistema.diminuir_quantidade(cod, qtd)

            transferencia = Transferencia(deposito, produtos)

            self.__transferencias.append(transferencia)

        except Exception as e:
            self.__tela_transferencia.mensagem_erro(e)

    def listar_transferencias(self):
        self.__tela_transferencia.mensagem("---- Transferencias ----")
        for transf in self.__transferencias:
            self.__tela_transferencia.info(transf)

    def buscar_transferenia(self):
        codigo = self.__tela_transferencia.buscar()

        try:
            for transf in self.__transferencias:
                if transf.codigo == codigo:
                    self.__tela_transferencia.info(transf)
                    return True
            raise TransferenciaNaoEncontrada(codigo)

        except Exception as e:
            self.__tela_transferencia.mensagem_erro(e)

    def abre_tela(self):
        lista_opcoes = {
            1: self.nova_transferencia(),
            2: self.listar_transferencias(),
            3: self.buscar_transferenia(),
            0: self.retornar(),
        }
        while True:
            lista_opcoes[self.__tela_transferencia.opcoes()]()
