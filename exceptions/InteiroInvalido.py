class InteiroInvalido(Exception):
    def __init__(self):
        super().__init__("Valor inválido! Digite um número inteiro.")
