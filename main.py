import math
import pandas as pd

from scripts.pre_analysis import cleanse_df, print_df_stats
from scripts.user_interaction import ask_yes_no, print_section

df = pd.read_csv('data/Sao_Paulo_housing_prices_20230501.csv')

if ask_yes_no(
    'Gostaria de verificar se os dados do dataset estão incoerentes? (N/s) \n--> ', 
    False
):
    print_df_stats(df)
    df = cleanse_df(df)

# Obter média e mediana dos aluguéis:
mean_rent = df['rent'].mean()
median_rent = df['rent'].median()

print_section("Aluguel - Informações Básicas", 
    "Valor médio dos aluguéis: " + f"R$ {mean_rent:.2f}" + 
    "\nValor mediano dos aluguéis: " + f"R$ {median_rent:.2f}"
)

# Identificar localidades (distritos) com quantidades consideráveis de registros:
districts = df['district'].value_counts()
FLOOR = 0.25 # Top 25% dos distritos
cutoff_count = districts.iloc[math.ceil(districts.size * FLOOR) - 1] # Resultará em 8
top_districts = districts.loc[districts >= cutoff_count].index

# Obter os distritos com o menor e maior preço médio, desde que tenham no mínimo 8 imóveis listados:
districts_mean_rent = (
    df.groupby('district')['rent']
    .mean()
    .rename('mean_rent') # type: ignore[arg-type] 
    .loc[top_districts]
    .sort_values(ascending=False)
    .reset_index() # Usa um índice numérico
)

highest_rent_district = districts_mean_rent.iloc[0]
lowest_rent_district = districts_mean_rent.iloc[-1]

print_section("Aluguel - Por distrito",
    f"Distrito com maior valor médio: {highest_rent_district['district']} (R$ {highest_rent_district['mean_rent']:.2f})" +
    f"\nDistrito com menor valor médio: {lowest_rent_district['district']} (R$ {lowest_rent_district['mean_rent']:.2f})" +
    f"\n\nOBS.: A quantidade mínima de imóveis que um distrito precisa ter para ser contabilizado nesta análise é {cutoff_count}."
)


print('|==== FIM DO PROGRAMA ====|')

