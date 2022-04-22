"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Visitor
"""

from abc import ABC, abstractmethod
from typing import List


class Visitor(ABC):
    """
    A interface Visitor deve ser implementada por classes visitantes
    """

    @abstractmethod
    def visit_carro(self, element: "Carro"):
        pass

    def visit_onibus(self, element: "Onibus"):
        pass


class Veiculo(ABC):
    """
    Veiculo é a raiz de uma hierarquia de classes
    Todas as classes dessa hierarquia aceitam (método accept) visitas de objetos "Visitor"
    Ou seja, Veiculos e suas subclasses estão abertas para tais visitas
    Mas elas não sabem exatamente o que o Visitor vai fazer com o seus dados
    """

    def __init__(self, placa: str):
        self._placa = placa

    def get_placa(self) -> str:
        return getattr(self, "_placa")

    @abstractmethod
    def accept(self, visitor: "Visitor") -> None:
        pass


class Carro(Veiculo):

    def __init__(self, placa: str):
        super().__init__(placa)

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_carro(self)


class Onibus(Veiculo):

    def __init__(self, placa: str):
        super().__init__(placa)

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_onibus(self)


class PrintVisitor(Visitor):
    """
    PrintVisitor é uma classe visitante
    Ela imprime a placa de Veiculos concretos (isto é, Carro e Onibus) na tela
    """

    def visit_carro(self, element: Carro) -> None:
        print(f"Visitando um Carro: {element.get_placa()}")

    def visit_onibus(self, element: Onibus) -> None:
        print(f"Visitando um Onibus: {element.get_placa()}")


class Main:

    @staticmethod
    def main() -> None:
        list: List[Veiculo] = [
            Carro("C1"), Onibus("01"),
            Carro("C2"), Onibus("02")
        ]

        # Vamos "visitar", com um PrintVisitor, cada Veiculo da lista
        visitor: PrintVisitor = PrintVisitor()

        for veiculo in list:
            veiculo.accept(visitor)

        # Benefício do padrão Visitor:
        # Podemos implementar uma outra classe Visitor sem ter que mexer na implementação
        # da classe Veiculo e de suas subclasses. Em seguinda, podemos usar esse Visitor
        # para visitar todos os veículos da nossa lista.


if __name__ == "__main__":
    Main.main()
