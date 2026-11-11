import json
import os


def salvar_json(dados):

    caminho_atual = os.path.dirname(
        os.path.abspath(__file__)
    )


    pasta_destino = os.path.join(
        caminho_atual,
        "..",
        "dados"
    )


    os.makedirs(
        pasta_destino,
        exist_ok=True
    )


    caminho_arquivo = os.path.join(
        pasta_destino,
        "dados_ibge.json"
    )


    with open(
        caminho_arquivo,
        "w",
        encoding="utf-8"
    ) as arquivo:


        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


    print(
        f"Arquivo salvo em: {caminho_arquivo}"
    )