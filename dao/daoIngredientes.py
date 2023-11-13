from dao.DAO import DAO
from model.Ingrediente import Ingrediente


class IngredienteDAO(DAO):
    def __init__(self):
        super().__init__('ingredientes.pkl')

    def add(self, ingrediente: Ingrediente):
        if ingrediente is not None and isinstance(ingrediente, Ingrediente) and isinstance(ingrediente.codigo, int):
            super().add(ingrediente.nome, ingrediente)

    def update(self, ingrediente: Ingrediente):
        if ingrediente is not None and isinstance(ingrediente, Ingrediente) and isinstance(ingrediente.codigo, int):
            super().update(ingrediente.codigo, int)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            return super().get(key)

