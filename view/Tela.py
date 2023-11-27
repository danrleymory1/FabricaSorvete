from abc import ABC, abstractmethod
from os import name, system
import PySimpleGUI as sg


class Tela(ABC):
    def limpar_tela(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    @abstractmethod
    def opcoes(self):
        pass

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
    def remover(self, value):
        pass

    @abstractmethod
    def alterar(self, value):
        pass

    def mensagem(self, texto):
        print(f"{texto}")

    def mensagem_sucesso(self, mensagem):
        sg.Popup(f"SUCESSO: {mensagem}")

    def mensagem_erro(self, mensagem):
        sg.Popup(f"ERRO: {mensagem}")

    def erro_tentar_novamente(self, mensagem):
        msg = f"{mensagem}\nDeseja tentar novamente?"

        return sg.Popup(msg, button_type=1)
