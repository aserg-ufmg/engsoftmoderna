"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Singleton
"""


class Logger(object):
    """
    A classe Logger é um Singleton.
    Logo, por construção, poderá existir no máximo uma instância (objeto)
    dessa classe.
    """

    # Instância única
    __instance = None

    def __new__(cls):
        """A cada chamada de Logger(), retorna a instância única"""
        # 1a vez que cria um objeto da classe
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __str__(self) -> str:
        """Retorna o id do singleton"""
        return hex(id(self))

    def println(self, msg) -> None:
        """registra msg na console, mas poderia ser em um arquivo"""
        print(msg)


class Main:

    def f(self) -> None:
        log: Logger = Logger()
        log.println(f"Executando f {log}")

    def g(self) -> None:
        log: Logger = Logger()
        log.println(f"Executando g {log}")

    def h(self) -> None:
        log: Logger = Logger()
        log.println(f"Executando h {log}")

    @staticmethod
    def main() -> None:
        m = Main()
        m.f()
        m.g()
        m.h()
        print(
            f"Observe que as 3 chamadas executaram no mesmo objeto, com ID: {Logger()}"
        )


if __name__ == "__main__":
    Main.main()
