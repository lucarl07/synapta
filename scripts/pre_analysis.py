# ==:== Limpeza Inicial dos Dados ==:==

import numpy as np

from pandas import DataFrame

def print_df_stats(df: DataFrame):
    """
    Imprime algumas informações do DataFrame, que podem ser importantes para ver inconsistências.
    """

    describe_number_cols = df.describe(include=[str])
    describe_option_cols = df.describe(include=[np.number])

    print("|==== INFORMAÇÕES GERAIS ====|")
    df.info() 
    print() # Print vazio para pular uma linha

    print(
        f"|==== ESTATÍSTICAS: Colunas Categóricas ====|\n {describe_number_cols}", 
        f"|==== ESTATÍSTICAS: Colunas Numéricas ====|\n {describe_option_cols}", 
        sep='\n\n', end='\n\n'
    )

def cleanse_df(df: DataFrame):
    """
    Recebe um DataFrame possivelmente impuro e retorna um DataFrame limpo, sem valores nulos e 
    duplicatas.
    """

    colunas = df.columns.values

    # Caso existirem valores nulos nas colunas categóricas:
    for coluna in colunas:
        if (df[coluna].dtype == 'object'):
            df[coluna] = df[coluna].fillna('Desconhecido')

    # Caso existirem valores nulos nas demais colunas (numéricas):
    df = df.dropna()

    # Caso existirem linhas duplicadas:
    df = df.drop_duplicates()

    # Para os imóveis com menos de 8 m² de área útil total (mínimo de acordo com a 
    # Lei nº 16.642/2017, da cidade de São Paulo):
    MIN_USABLE_AREA = 8 
    df = df.filter(cond=df['area'] >= MIN_USABLE_AREA) 

    # Para os imóveis que não são SKs (SK = Studio ou kitnet) com 0 quartos:
    MIN_BEDROOMS_FOR_NON_SKs = 1

    no_bedroom_nor_is_sk_idx = df[
        (df["type"] != "Studio e kitnet") & 
        (df["bedrooms"] < MIN_BEDROOMS_FOR_NON_SKs)
    ].index

    df = df.drop(no_bedroom_nor_is_sk_idx)

    print("Limpeza efetuada com sucesso.")
    
    return df

