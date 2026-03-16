import requests

class Extract:
    """
    Classe responsável por extrair dados de universidades
    a partir de uma API pública.
    """

    def __init__(self):
        pass

    def extract_country(self, country):
        """
        Faz uma requisição à API de universidades filtrando por país.

        Args:
            country (str): Nome do país para buscar as universidades.

        Returns:
            list: Lista de dicionários com os dados das universidades.
        """

        # Monta a URL da API com o país informado como parâmetro de busca
        url = f"http://universities.hipolabs.com/search?country={country}"

        # Realiza a requisição GET à API
        response = requests.get(url)

        # Lança uma exceção caso a requisição retorne um erro HTTP
        response.raise_for_status()

        # Converte a resposta JSON em uma lista de dicionários
        universities = response.json()

        return universities
