import requests


def buscar_municipios():

    url = (
        "https://servicodados.ibge.gov.br/"
        "api/v1/localidades/municipios"
    )


    resposta = requests.get(url)


    if resposta.status_code == 200:

        return resposta.json()


    raise Exception(
        "Erro ao consultar API do IBGE"
    )