class ReceitaInvalida(Exception):
    def __init__(self, codigo, quantidade):
        if quantidade < 1:
            super().__init__(f"Erro na receita: quantidade inválida ({quantidade})")
        else:
            super().__init__(
                f"Erro na receita: código de ingrediente inválido ({codigo})"
            )
