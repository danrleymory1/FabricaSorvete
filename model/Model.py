from abc import ABC, abstractmethod


class BaseModel(ABC):
    auto_codigo = 1

    def __init__(self):
        self.__codigo = self.__class__.auto_codigo
        self.__class__.auto_codigo += 1

    @property
    def codigo(self):
        return self.__codigo
