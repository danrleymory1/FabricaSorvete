class IngredienteInsuficiente(Exception):
    def __init__(self, nome, desejada, existente):
        super().__init__(
            f"Receita precisa de {desejada} {nome}s, mas apenas {existente} no estoque"
        )
