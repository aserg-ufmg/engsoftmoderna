from json import loads
from typing import Any, Dict
from urllib.request import urlopen
"""
Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
Prof. Marco Tulio Valente

Exemplo do padrão de projeto Fachada
"""

# Exemplos de APIs não tão simples
# Pois para obter dados como altura e cor de pele
# Foi necessário para o cliente fazer um request http
# deserializar o retorno e procurar pelo dado


def getLukeSkywalkerHeight():
    """
    Retorna a altura de Luke Skywalker
    """
    url = "https://swapi.dev/api/people/1/"
    response = urlopen(url)
    data = response.read()
    deserialized_data = loads(data)
    return deserialized_data["height"]


def getC3POSkinColor():
    """
    Retorna a cor da pele de C-3PO
    """
    url = "https://swapi.dev/api/people/2/"
    response = urlopen(url)
    data = response.read()
    deserialized_data = loads(data)
    return deserialized_data["skin_color"]


class StarWarsFacade:
    """
    Fachada para obter informações de Star Wars
    """

    def __init__(self, api_endpoint: str) -> None:
        self._api_endpoint = api_endpoint

    def _make_request(self, url: str) -> str:
        response = urlopen(url)
        return response.read()

    def _parse_return(self, ret: str) -> Dict[str, Any]:
        return loads(ret)

    def get_info(self, person: str, field: str) -> str:
        url = f"{self._api_endpoint}/people/{person}"
        ret = self._make_request(url)
        data = self._parse_return(ret)
        return data[field]


class Main:

    @staticmethod
    def main() -> None:
        # Essa interface é mais simples que os códigos
        # contidos nas funções correspondentes
        # luke_height = getLukeSkywalkerHeight()
        # c3p0_skin = getC3POSkinColor()

        facade = StarWarsFacade("https://swapi.dev/api/")
        luke_height = facade.get_info("1", "height")
        c3p0_skin = facade.get_info("2", "skin_color")
        print(f"Luke's height: {luke_height}\n"
              f"C-3PO's skin color: {c3p0_skin}")


if __name__ == "__main__":
    Main.main()
