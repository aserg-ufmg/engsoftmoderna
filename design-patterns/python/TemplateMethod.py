"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Template Method
"""

from abc import ABC, abstractmethod


class Funcionario(ABC):
    """
    Classe que implementa um Template Method (calcSalarioLiquido)
    Veja que essa classe é abstrata
    """

    def __init__(self, salario):
        self._salario = salario

    @abstractmethod
    def calcDescontosPrevidencia(self) -> float:
        pass

    @abstractmethod
    def calcDescontosPlanoSaude(self) -> float:
        pass

    @abstractmethod
    def calcOutrosDescontos(self) -> float:
        pass

    def calcSalarioLiquido(self) -> float:
        """
        Template Method: define o esqueleto de um algoritmo
        Ele ainda é um "template" porque os métodos chamados são abstratos
        """
        prev: float = self.calcDescontosPrevidencia()
        saude: float = self.calcDescontosPlanoSaude()
        outros: float = self.calcOutrosDescontos()

        return self._salario - prev - saude - outros


class FuncionarioCLT(Funcionario):
    """
    Classe que implementa um Template Method (calcDescontosPrevidencia)
    """

    def __init__(self, salario):
        super().__init__(salario)

    def calcDescontosPrevidencia(self) -> float:
        """
        implementação do método abstrato
        """
        return self._salario * 0.01

    def calcDescontosPlanoSaude(self) -> float:
        """
        implementação do método abstrato
        """
        return 100.0

    def calcOutrosDescontos(self) -> float:
        """
        implementação do método abstrato
        """
        return 20.0


class Main:

    @staticmethod
    def main() -> None:
        """
        Método principal
        """
        func: FuncionarioCLT = FuncionarioCLT(1000.0)
        salario: float = func.calcSalarioLiquido()
        print(f"Salário Líquido: {salario}")


if __name__ == "__main__":
    Main.main()
