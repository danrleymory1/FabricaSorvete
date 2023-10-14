class SabornoSistema(Exception):
    def __init__(self):
        super().__init__("Já existe o sabor no sistema com essa descricao.")
