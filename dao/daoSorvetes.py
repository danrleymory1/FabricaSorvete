from dao.DAO import DAO
from model.Sorvete import Sorvete

class SorveteDAO(DAO):
    def __init__(self):
        super().__init__('sorvetes.pkl')

    def add(self, sorvete: Sorvete):
        if sorvete is not None and isinstance(sorvete, Sorvete) and isinstance(sorvete.codigo, int):
            super().add(sorvete.codigo, sorvete)

    def update(self, sorvete: Sorvete):
        if sorvete is not None and isinstance(sorvete, Sorvete) and isinstance(sorvete.codigo, int):
            super().update(sorvete.codigo, int)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            return super().get(key)
