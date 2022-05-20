"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Observador
"""

from abc import ABC


class Subject:
    """
    Classe Subject (que faz parte da implementação interna do padrão)
    Todo sujeito deve herdar dessa classe
    Ela inclui métodos para adicionar, remover e notificar os
    observadores desse sujeito
    """

    def __init__(self):
        self.observers = []

    def add_observer(self, observer: "Observer") -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: "Observer") -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self) -> None:
        """
        Notifica todos os observadores do sujeito
        """
        for observer in self.observers:
            observer.update(self)


class Observer(ABC):
    """
    Interface Observer (também faz parte da implementação interna do padrão)
    Todo observador deve implementar essa interface
    """

    def update(self, subject: "Subject") -> None:
        """
        Método que será implementado pelos observadores
        """
        pass


class Temperatura(Subject):
    """
    Temperatura são sujeitos (isto é, objetos que podem ser observados)
    """

    def __init__(self, temperatura: float) -> None:
        super().__init__()
        self._temperatura = temperatura

    def get_temp(self) -> float:
        return getattr(self, "_temperatura")

    def set_temp(self, temperatura: float) -> None:
        self._temperatura = temperatura
        self.notifyObservers()


class TermometroCelsius(Observer):
    """
    TermometroCelsius são observadores (de Temperatura)
    """

    def update(self, subject) -> None:
        temp: float = subject.get_temp()
        print(f"Temperatura Celsius: {temp}ºC")


class Main:

    @staticmethod
    def main() -> None:
        t: Temperatura = Temperatura(0)
        t.add_observer(TermometroCelsius())
        t.set_temp(100.0)


if __name__ == "__main__":
    Main.main()
