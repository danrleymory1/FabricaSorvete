from dao.DAO import DAO
from model.Ingrediente import Ingrediente


class IngredienteDAO(DAO):
    def __init__(self):
        super().__init__("ingredientes.pkl")

    def add(self, ingrediente: Ingrediente):
        if (
            ingrediente is not None
            and isinstance(ingrediente, Ingrediente)
            and isinstance(ingrediente.nome, str)
        ):
            super().add(ingrediente.codigo, ingrediente)

    def update(self, ingrediente: Ingrediente):
        if (
            ingrediente is not None
            and isinstance(ingrediente, Ingrediente)
            and isinstance(ingrediente.codigo, str)
        ):
            super().update(ingrediente.codigo, ingrediente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, ingrediente: Ingrediente):
        if (
            ingrediente is not None
            and isinstance(ingrediente, Ingrediente)
            and isinstance(ingrediente.codigo, str)
        ):
            return super().remove(ingrediente.codigo)
