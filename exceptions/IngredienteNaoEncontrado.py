class IngredienteNaoEncontrado(Exception):
    def __init__(self, codigo):
        super().__init__(f"Ingrediente com código {codigo} não encontrado")
