class IngredienteDiminuirInsuficiente(Exception):
    def __init__(self, nome, quantidade):
        super().__init__(f'Apenas {quantidade} "{nome}" no sistema')
