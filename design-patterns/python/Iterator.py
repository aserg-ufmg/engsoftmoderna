"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Iterator
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any, List


class IteradorListaPalavras(Iterator):
    """
    Iterador concreto de uma coleção de palavras.
    """
    """
    Estado interno do iterador
    """
    _posicao: int = 0
    _reverso: bool = False

    def __init__(self, palavras: ListaPalavras, reverso: bool = False) -> None:
        self._palavras = palavras
        self._reverso = reverso
        self._posicao = -1 if reverso else 0

    def __next__(self):
        """
        Retorna a próxima palavra da lista. Ou StopIteration se não houver mais.
        """
        try:
            item: str = self._palavras[self._posicao]
            self._posicao += -1 if self._reverso else 1
        except IndexError:
            raise StopIteration()

        return item


class ListaPalavras(Iterable):
    """
    Coleção que contém palavras
    """

    def __init__(self, palavras: List[str] = []) -> None:
        self._palavras = palavras

    def __getitem__(self, index: int) -> str:
        return self._palavras[index]

    def __iter__(self) -> IteradorListaPalavras:
        """
        Retorna o iterador da coleção em ordem normal por padrão
        """
        return IteradorListaPalavras(self)

    def get_reverse_iterator(self) -> IteradorListaPalavras:
        """
        Retorna o iterador da coleção em ordem reversa
        """
        return IteradorListaPalavras(self, True)

    def add_item(self, item: str):
        self._palavras.append(item)


class Main:

    @staticmethod
    def main() -> None:
        """
        Método principal
        """

        palavras: ListaPalavras = ListaPalavras(
            ["Palavra01", "Palavra02", "Palavra03"])
        palavras.add_item("Palavra04")
        palavras.add_item("Palavra05")

        print(f"Iterando em ordem normal: {', '.join(palavras)}")
        print(
            f"Iterando em ordem reversa: {', '.join(palavras.get_reverse_iterator())}"
        )


if __name__ == "__main__":
    Main.main()
