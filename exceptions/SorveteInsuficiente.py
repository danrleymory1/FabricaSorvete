class SorveteInsuficiente(Exception):
    def __init__(self, nome, desejada, existente):
        super().__init__(
            f'Preicsa de {desejada} "{nome}", mas apenas {existente} no estoque'
        )
