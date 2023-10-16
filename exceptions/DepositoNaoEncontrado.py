class DepositoNaoEncontrado(Exception):
    def __init__(self, codigo):
        super().__init__(f"Depósito com código {codigo} não encontrado")
