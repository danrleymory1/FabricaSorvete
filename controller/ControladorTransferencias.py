import datetime
from dao.daoTransferencias import TransferenciaDAO
from exceptions.DepositoNaoEncontrado import DepositoNaoEncontrado
from exceptions.SorveteNaoEncontrado import SorveteNaoEncontrado
from exceptions.SorveteInsuficiente import SorveteInsuficiente
from exceptions.TransferenciaNaoEncontrada import TransferenciaNaoEncontrada
from view.TelaTransferencia import TelaTransferencia
from model.Transferencia import Transferencia


class ControladorTransferencias:
    def __init__(self, controlador_sistema):
        self.__transferencias = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_transferencia = TelaTransferencia()
        self.__transferencias_dao = TransferenciaDAO()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def nova_transferencia(self):
        depositos = (
            self.__controlador_sistema.controlador_depositos.depositos_dao.get_all()
        )

        sorvetes = (
            self.__controlador_sistema.controlador_sorvetes.sorvetes_dao.get_all()
        )

        depositos_dict = [d.descricao for d in depositos]
        sorvetes_dict = [s.sabor for s in sorvetes]

        vals = self.__tela_transferencia.adicionar(depositos_dict, sorvetes_dict)

        if vals == None:
            return

        deposito_dest, sorvete_qtd_dict = vals

        sorvetes_quantidades = []
        for sabor, qtd in sorvete_qtd_dict.items():
            try:
                for s in sorvetes:
                    if s.sabor == sabor:
                        s_q = {"sorvete": s, "quantidade": qtd}

                        nova_quantidade = s.quantidade - qtd
                        if nova_quantidade < 0:
                            raise SorveteInsuficiente(s.sabor, qtd, s.quantidade)

                        s.quantidade = nova_quantidade
                        self.__controlador_sistema.controlador_sorvetes.sorvetes_dao.update(
                            s
                        )
                        sorvetes_quantidades.append(s_q)

            except Exception as e:
                self.__tela_transferencia.mensagem_erro(e)
                return

        deposito_nova_transf = None
        for deposito in depositos:
            if deposito.descricao == deposito_dest:
                deposito_nova_transf = deposito

        transf = Transferencia(deposito_nova_transf, sorvetes_quantidades)

        self.__transferencias_dao.add(transf)

        self.__tela_transferencia.mensagem_sucesso("Transferência feita com sucesso")

    def listar_transferencias(self):
        transferencias = self.__transferencias_dao.get_all()

        self.__tela_transferencia.info(self.preparar_para_tela(transferencias))

    def buscar_transferenia(self):
        val = self.__tela_transferencia.buscar()

        if val is None:
            return

        transferencias = self.__transferencias_dao.get_all()

        data_inicio = None
        data_fim = None

        if (val["data_inicio"] is not None) and (val["data_inicio"].strip() != ""):
            d, m, y = val["data_inicio"].split("/")
            data_inicio = datetime.datetime(year=int(y), day=int(d), month=int(m))

        if (val["data_fim"] is not None) and (val["data_fim"].strip() != ""):
            d, m, y = val["data_fim"].split("/")
            data_fim = datetime.datetime(year=int(y), day=int(d), month=int(m))

        if val["opcao"] == "Produto":
            res = []
            produto = val["info"]
            for t in transferencias:
                for p in t.produtos:
                    if produto.upper() in p["sorvete"].sabor.upper():
                        if data_inicio and data_fim:
                            if (
                                t.data >= data_inicio
                                and t.data <= data_fim + datetime.timedelta(days=1)
                            ):
                                res.append(t)
                        elif data_inicio:
                            if t.data >= data_inicio:
                                res.append(t)
                        elif data_fim:
                            if t.data <= data_fim + datetime.timedelta(days=1):
                                res.append(t)
                        else:
                            res.append(t)

            self.__tela_transferencia.info(self.preparar_para_tela(res))

        if val["opcao"] == "Depósito":
            res = []
            deposito = val["info"]
            for t in transferencias:
                if deposito.upper() in t.deposito_dest.descricao.upper():
                    if data_inicio and data_fim:
                        if t.data >= data_inicio and t.data <= data_fim:
                            res.append(t)
                    elif data_inicio:
                        if t.data >= data_inicio:
                            res.append(t)
                    elif data_fim:
                        if t.data >= data_fim:
                            res.append(t)
                    else:
                        res.append(t)

            self.__tela_transferencia.info(self.preparar_para_tela(res))

    def abre_tela(self):
        lista_opcoes = {
            1: self.nova_transferencia,
            2: self.listar_transferencias,
            3: self.buscar_transferenia,
            0: self.retornar,
        }
        while True:
            lista_opcoes[self.__tela_transferencia.opcoes()]()

    def preparar_para_tela(self, transferencias):
        transferencias_tela = []

        for transf in transferencias:
            sorvetes = []

            for sorv in transf.produtos:
                sorvetes.append(
                    {"sorvete": sorv["sorvete"].sabor, "quantidade": sorv["quantidade"]}
                )

            transf_dict = transf.__dict__.copy()
            transf_dict["_Transferencia__produtos"] = sorvetes
            transf_dict["_Transferencia__data"] = transf.data.strftime("%d/%m/%Y")
            transf_dict[
                "_Transferencia__deposito_dest"
            ] = transf.deposito_dest.descricao
            transferencias_tela.append(transf_dict)

        return transferencias_tela
