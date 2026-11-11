from api_ibge import buscar_municipios
from tratamento import preparar_dataframe
from analise import gerar_indicadores
from exportar import salvar_json



def executar():


    print("Consultando IBGE...")


    dados = buscar_municipios()



    print("Tratando dados...")


    dataframe = preparar_dataframe(dados)



    print("Gerando análises...")


    indicadores = gerar_indicadores(
        dataframe
    )



    print("Exportando JSON...")


    salvar_json(indicadores)



    print(
        "Processo finalizado!"
    )



if __name__ == "__main__":

    executar()