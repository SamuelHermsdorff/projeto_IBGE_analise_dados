def gerar_indicadores(df):


    total_municipios = len(df)



    estados = (
        df
        .groupby("estado")
        .size()
        .sort_values(
            ascending=False
        )
    )


    regioes = (
        df
        .groupby("regiao")
        .size()
        .sort_values(
            ascending=False
        )
    )



    estado_maior = estados.index[0]

    quantidade_maior = int(
        estados.iloc[0]
    )



    estado_menor = estados.index[-1]

    quantidade_menor = int(
        estados.iloc[-1]
    )



    resultado = {


        "indicadores": {


            "total_municipios":
            total_municipios,


            "estado_maior_quantidade": {


                "nome":
                estado_maior,


                "quantidade":
                quantidade_maior

            },


            "estado_menor_quantidade": {


                "nome":
                estado_menor,


                "quantidade":
                quantidade_menor

            }


        },



        "graficos": {


            "municipios_por_estado":

            [

                {

                    "estado": estado,

                    "quantidade":
                    int(valor)

                }

                for estado, valor
                in estados.items()

            ],



            "municipios_por_regiao":

            [

                {

                    "regiao": regiao,

                    "quantidade":
                    int(valor)

                }

                for regiao, valor
                in regioes.items()

            ]

        }



    }


    return resultado