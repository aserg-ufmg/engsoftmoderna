"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Fábrica
"""
from abc import ABC

# Objetos que serão fabricados


class Channel(ABC):
    """
    Classe abstrata de canal
    """

    pass


class TCPChannel(Channel):
    """
    Canal TCP
    """

    pass


class UDPChannel(Channel):
    """
    Canal UDP
    """

    pass


class ChannelFactory:
    """
    A classe ChannelFactory implementa um método fábrica estático.
    Isto é, um método que centraliza a criação de objetos que
    implementam a interface Channel

    Se amanhã quisermos que o sistema use UDPChannel, basta
    mudar a implementação de create()
    """

    @staticmethod
    def create() -> Channel:
        """
        Método fábrica estático
        """
        print("Neste momento, estamos trabalhando com TCPChannel")
        return TCPChannel()


class Main:

    def f(self) -> None:
        c: Channel = ChannelFactory.create()

    def g(self) -> None:
        c: Channel = ChannelFactory.create()

    def h(self) -> None:
        c: Channel = ChannelFactory.create()

    @staticmethod
    def main() -> None:
        m = Main()
        m.f()
        m.g()
        m.h()


if __name__ == "__main__":
    Main.main()
