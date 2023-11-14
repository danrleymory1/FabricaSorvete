class ReceitaInvalida(Exception):
    def __init__(self, ingrediente, quantidade):
        super().__init__(
            f"Erro na receita: quantidade do ingrediente {ingrediente.nome} inválida ({quantidade})"
        )
