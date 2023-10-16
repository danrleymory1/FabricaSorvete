class SorveteNaoEncontrado(Exception):
    def __init__(self, codigo):
        super().__init__(f"Sorvete com código {codigo} não encontrado")
