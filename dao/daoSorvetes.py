from dao.DAO import DAO
from model.Sorvete import Sorvete


class SorveteDAO(DAO):
    def __init__(self):
        super().__init__("sorvetes.pkl")

    def add(self, sorvete: Sorvete):
        if (
            sorvete is not None
            and isinstance(sorvete, Sorvete)
            and isinstance(sorvete.codigo, str)
        ):
            super().add(sorvete.codigo, sorvete)

    def update(self, sorvete: Sorvete):
        if (
            sorvete is not None
            and isinstance(sorvete, Sorvete)
            and isinstance(sorvete.codigo, str)
        ):
            super().update(sorvete.codigo, sorvete)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, sorvete: Sorvete):
        if (
            sorvete is not None
            and isinstance(sorvete, Sorvete)
            and isinstance(sorvete.codigo, str)
        ):
            return super().remove(sorvete.codigo)
