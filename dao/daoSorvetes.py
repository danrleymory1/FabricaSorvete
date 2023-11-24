from uuid import UUID
from dao.DAO import DAO
from model.Sorvete import Sorvete


class SorveteDAO(DAO):
    def __init__(self):
        super().__init__("sorvetes.pkl")

    def add(self, sorvete: Sorvete):
        if (
            sorvete is not None
            and isinstance(sorvete, Sorvete)
            and isinstance(sorvete.codigo, UUID)
        ):
            super().add(sorvete.codigo, sorvete)

    def update(self, sorvete: Sorvete):
        if (
            sorvete is not None
            and isinstance(sorvete, Sorvete)
            and isinstance(sorvete.codigo, UUID)
        ):
            super().update(sorvete.codigo, UUID)

    def get(self, key: UUID):
        if isinstance(key, UUID):
            return super().get(key)

    def remove(self, key: UUID):
        if isinstance(key, UUID):
            return super().get(key)
