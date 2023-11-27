from dao.DAO import DAO
from model.Transferencia import Transferencia


class TransferenciaDAO(DAO):
    def __init__(self):
        super().__init__("transferencias.pkl")

    def add(self, transferencia: Transferencia):
        if (
            transferencia is not None
            and isinstance(transferencia, Transferencia)
            and isinstance(transferencia.codigo, str)
        ):
            super().add(transferencia.codigo, transferencia)

    def update(self, transferencia: Transferencia):
        if (
            transferencia is not None
            and isinstance(transferencia, Transferencia)
            and isinstance(transferencia.codigo, str)
        ):
            super().update(transferencia.codigo, transferencia)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, transferencia: Transferencia):
        if (
            transferencia is not None
            and isinstance(transferencia, Transferencia)
            and isinstance(transferencia.codigo, str)
        ):
            return super().remove(transferencia.codigo)
