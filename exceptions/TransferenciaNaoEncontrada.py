class TransferenciaNaoEncontrada(Exception):
    def __init__(self, codigo):
        super().__init__(f"Transfêrencia com código {codigo} não encontrada")
