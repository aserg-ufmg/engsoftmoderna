"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Strategy
"""

from abc import ABC, abstractmethod
from typing import List


class SortStrategy(ABC):
    """
    Classes que implementam estratégias de ordenação devem herdar
    de SortStrategy e implementar o método sort
    """

    @abstractmethod
    def sort(self, elementos: List[int]) -> None:
        pass


class BubbleSortStrategy(SortStrategy):
    """
    Classe que implementa sort usando o algoritmo Bubble Sort
    """

    def sort(self, elementos: List[int]) -> None:
        n: int = len(elementos)
        temp: int = 0
        for i in range(n):
            for j in range(0, n - i - 1):
                if elementos[j] > elementos[j + 1]:
                    temp = elementos[j]
                    elementos[j] = elementos[j + 1]
                    elementos[j + 1] = temp


class SelectionSortStrategy(SortStrategy):
    """
    Classe que implementa sort usando o algoritmo Selection Sort
    """

    def sort(self, elementos: List[int]) -> None:
        for i in range(len(elementos)):
            min_index: int = i
            for j in range(i + 1, len(elementos)):
                if elementos[min_index] > elementos[j]:
                    min_index = j
            elementos[i], elementos[min_index] = elementos[
                min_index], elementos[i]


class MyList:
    """
    A classe MyList implementa uma lista que permite mudar sua "estratégia" de ordenação
    No vocabulário de design patterns, "estratégia" = algoritmo
    """

    def __init__(self, elementos: List[int]):
        self._elementos = elementos
        # estratégia de ordenação
        # por padrão, a estratégia é a BubbleSort
        self._strategy = BubbleSortStrategy()

    def setSortStrategy(self, strategy: SortStrategy) -> None:
        """
        permite mudar estratégia de ordenação
        """
        self._strategy = strategy

    def sort(self) -> None:
        self._strategy.sort(self._elementos)

    def print(self) -> None:
        print(self._elementos)


class Main:

    @staticmethod
    def main() -> None:
        print("Lista #1 foi ordenada com a estratégia default: BubbleSort")
        list1: MyList = MyList([3, 5, 2, 4, 1, 6])
        list1.sort()
        list1.print()

        print(
            "\nLista #2 foi ordenada com uma outra estratégia: SelectionSort")
        list2: MyList = MyList([6, 5, 4, 3, 2, 1])
        list2.setSortStrategy(SelectionSortStrategy())
        list1.sort()
        list1.print()


if __name__ == "__main__":
    Main.main()
