from abc import ABC, abstractmethod


class Tela(ABC):
    @abstractmethod
    def opcoes(self):
        pass

    def opcao_input(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    @abstractmethod
    def buscar(self):
        pass

    @abstractmethod
    def info(self, objeto):
        pass

    @abstractmethod
    def adicionar(self):
        pass

    @abstractmethod
    def remover(self):
        pass

    @abstractmethod
    def alterar(self):
        pass

    def mensagem_sucesso(self, mensagem):
        print(f"SUCESSO: {mensagem}")

    def mensagem_erro(self, mensagem):
        print(f"ERRO: {mensagem}")
