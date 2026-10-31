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
    
    return df

