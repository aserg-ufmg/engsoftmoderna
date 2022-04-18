"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Decorador
"""
from abc import ABC, abstractmethod


class Channel(ABC):
    """
    Decoradores implementam sempre a interface Channel
    """

    @abstractmethod
    def send(self, msg: str) -> None:
        pass

    @abstractmethod
    def receive(self) -> str:
        pass


class TCPChannel(Channel):
    """
    TCPChannel é uma canal de comunicação concreto (que usa protocolo TCP)
    E, por isso, é a classe final de uma cadeia de decoradores
    """

    def send(self, msg: str) -> None:
        print(f"Canal concreto (TCP) enviando > {msg}")

    def receive(self) -> str:
        print(f"Canal concreto (TCP) recebendo...")
        return "José"


class ChannelDecorator(Channel):
    """
    Todos os decoradores são subclasse de ChannelDecorator
    """

    def __init__(self, channel: Channel) -> None:
        self._channel = channel

    def send(self, msg: str) -> None:
        self._channel.send(msg)

    def receive(self) -> str:
        return self._channel.receive()


class ZipChannel(ChannelDecorator):
    """
    Decorador que:
     - compacta mensagens antes de enviar (send)
     - descompacta mensagens depois de receber (receiver)
    """

    def __init__(self, channel: Channel) -> None:
        super().__init__(channel)

    def send(self, msg: str) -> None:
        print(f"Decorador compactando > {msg}")
        super().send(msg)

    def receive(self) -> str:
        msg = super().receive()
        print(f"Decorador descompactando > {msg}")
        return msg


class Main:

    @staticmethod
    def main() -> None:
        c: Channel = ZipChannel(TCPChannel())
        c.send("Qual seu nome?")
        r: str = c.receive()
        print(r)


if __name__ == "__main__":
    Main.main()
