"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Proxy
"""
from abc import ABC, abstractmethod


class Book:
    """
    Classe auxiliar
    """

    def __init__(self, name: str):
        self.name = name


class BookSearchInterface(ABC):
    """
    Interface implementada pelo objeto base e pelo Proxy
    """

    @abstractmethod
    def getBook(self, ISBN: str) -> Book:
        pass


class BookSearch(BookSearchInterface):
    """
    Classe do objeto base
    """

    def getBook(self, ISBN: str) -> Book | None:
        print(f"Pesquisando no objeto base - ISBN {ISBN}")
        if ISBN == "2":
            return Book("Gof")

        return None


class BookSearchProxy(BookSearchInterface):
    """
    Classe do Proxy
    """

    def __init__(self, base: BookSearchInterface):
        self.__base = base

    def getBook(self, ISBN: str) -> Book | None:
        book = None
        print(f"Entrando no proxy - ISBN {ISBN}")

        # A ideia aqui é que o Proxy conhece o livro que tem ISBN 1
        # Logo, ele nem precisa fazer a consulta ao objeto base
        if ISBN == "1":
            print(f"Livro achado no proxy - ISBN: {ISBN}")
            book = Book("ESM")
        else:
            print(
                f"Livro não achado no proxy; repassando chamada para objeto base - ISBN: {ISBN}"
            )
            book = self.__base.getBook(ISBN)

        print("Saindo do Proxy")
        return book


class Main:

    @staticmethod
    def main() -> None:
        bs: BookSearch = BookSearch()
        pbs: BookSearchInterface = BookSearchProxy(bs)

        b1: Book = pbs.getBook("1")
        print("===============")
        b2: Book = pbs.getBook("2")


if __name__ == "__main__":
    Main.main()
