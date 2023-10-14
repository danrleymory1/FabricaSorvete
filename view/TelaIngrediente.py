from view.Tela import Tela


class TelaIngrediente(Tela):
    def __init__(self):
        pass

    def opcoes(self):
        return "ok"

    def buscar(self):
        return 0

    def info(self, objeto):
        return "ok"

    def adicionar(self):
        return "ok"

    def remover(self):
        return "ok"

    def alterar(self):
        return (0, "ok")
