"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Adaptador
"""

from abc import ABC, abstractmethod


class ProjetorSamsung:
    """
    Classe concreta, representando um projetor da Samsung
    """

    def turnOn(self) -> None:
        print("Ligando projetor da Samsung")


class ProjetorLG:
    """
    Classe concreta, representando um projetor da LG
    """

    def enable(self, timer: int) -> None:
        print(f"Ligando projetor da LG em {timer} minutos")


class Projetor(ABC):
    """
    Interface para "abstrair" o tipo de projetor (Samsung ou LG)
    """

    @abstractmethod
    def liga(self) -> None:
        pass


class AdaptadorProjetorSamsung(Projetor):
    """
    Adaptador de ProjetorSamsung para Projetor
    Um objeto da classe a seguir é um Projetor (pois implementa essa interface),
    mas internamente repassa toda chamada de método para o objeto adaptado
    (no caso, um ProjetorSamssung)
    """

    def __init__(self, projetor: ProjetorSamsung) -> None:
        self.__projetor = projetor

    def liga(self) -> None:
        self.__projetor.turnOn()


class AdaptadorProjetorLG(Projetor):
    """
    Idem classe anterior, mas agora adaptando ProjetoLG para Projetor
    """

    def __init__(self, projetor: ProjetorLG) -> None:
        self.__projetor = projetor

    def liga(self) -> None:
        self.__projetor.enable(0)


class SistemaControleProjetores:
    """
    Classe que controla os projetores
    """

    def init(self, projetor: Projetor) -> None:
        projetor.liga()


class Main:

    @abstractmethod
    def main() -> None:
        samsung = AdaptadorProjetorSamsung(ProjetorSamsung())
        lg = AdaptadorProjetorLG(ProjetorLG())
        scp = SistemaControleProjetores()

        scp.init(samsung)
        scp.init(lg)


if __name__ == "__main__":
    Main.main()
