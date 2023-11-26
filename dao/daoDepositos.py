from dao.DAO import DAO
from model.Deposito import Deposito


class DepositoDAO(DAO):
    def __init__(self):
        super().__init__("depositos.pkl")

    def add(self, deposito: Deposito):
        if (
            deposito is not None
            and isinstance(deposito, Deposito)
            and isinstance(deposito.descricao, str)
        ):
            super().add(deposito.codigo, deposito)

    def update(self, deposito: Deposito):
        if (
            deposito is not None
            and isinstance(deposito, Deposito)
            and isinstance(deposito.codigo, str)
        ):
            super().update(deposito.codigo, deposito)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, deposito: Deposito):
        if (
            deposito is not None
            and isinstance(deposito, Deposito)
            and isinstance(deposito.codigo, str)
        ):
            return super().remove(deposito.codigo)
