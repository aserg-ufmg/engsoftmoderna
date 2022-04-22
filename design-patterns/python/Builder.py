"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Builder
"""


class Livro:

    def __init__(self,
                 nome: str = "",
                 autores: str = "",
                 editora: str = "",
                 ano: str = ""):
        self._nome = nome
        self._autores = autores
        self._editora = editora
        self._ano = ano

    def __str__(self):
        return f"{self._nome}, {self._autores}, {self._editora}, {self._ano}"

    class Builder:
        """
        Livro.Builder é uma classe interna, pública e estática de Livro.
        Por isso, é que podemos chamar "new Livro.Builder()" diretamente,
        sem precisar de instanciar antes um objeto do tipo Livro.
        """

        def __init__(self):
            self._nome = ""
            self._autores = ""
            self._editora = ""
            self._ano = ""

        def set_nome(self, nome: str):
            self._nome = nome
            return self

        def set_autores(self, autores: str):
            self._autores = autores
            return self

        def set_editora(self, editora: str):
            self._editora = editora
            return self

        def set_ano(self, ano: str):
            self._ano = ano
            return self

        def build(self):
            return Livro(self._nome, self._autores, self._editora, self._ano)


class Main:

    @staticmethod
    def main() -> None:
        """
        Método principal
        """

        esm: Livro = (
            Livro.Builder().set_nome("Engenharia de Software Moderna").
            set_editora("UFMG").set_ano("2020").build())

        print(f"Livro 1: {esm}")

        gof: Livro = (Livro.Builder().set_nome("Design Patterns").set_autores(
            "Gof").set_ano("1995").build())

        print(f"Livro 2: {gof}")


if __name__ == "__main__":
    Main.main()
