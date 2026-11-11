import pandas as pd


def preparar_dataframe(dados):

    municipios = []


    for item in dados:

        microrregiao = item.get("microrregiao")


        estado = "Não informado"
        regiao = "Não informado"


        if microrregiao:

            mesorregiao = microrregiao.get(
                "mesorregiao"
            )


            if mesorregiao:

                uf = mesorregiao.get("UF")


                if uf:

                    estado = uf.get(
                        "sigla",
                        "Não informado"
                    )


                    regiao_info = uf.get(
                        "regiao"
                    )


                    if regiao_info:

                        regiao = regiao_info.get(
                            "nome",
                            "Não informado"
                        )


        municipios.append({

            "id": item.get("id"),

            "municipio": item.get(
                "nome",
                "Não informado"
            ),

            "estado": estado,

            "regiao": regiao

        })


    df = pd.DataFrame(municipios)


    return df