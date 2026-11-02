import math
import pandas as pd

from scripts.pre_analysis import cleanse_df, print_df_stats
from scripts.user_interaction import ask_yes_no, print_section

# ==:== Configurações do Pandas ==:==
pd.options.display.float_format = '{:.2f}'.format

# Ler DataFrame:
df = pd.read_csv('data/Sao_Paulo_housing_prices_20230501.csv')

# Verificação e limpeza opcionais:
if ask_yes_no(
    'Gostaria de verificar se os dados do dataset estão incoerentes? (N/s) \n--> ', 
    False
):
    df = cleanse_df(df)
    print_df_stats(df)

# Obter média e mediana dos aluguéis:
mean_rent = df['rent'].mean()
median_rent = df['rent'].median()

print_section("Aluguel - Informações Básicas", 
    "Valor médio dos aluguéis (R$): " + f"{mean_rent:.2f}" + 
    "\nValor mediano dos aluguéis (R$): " + f"{median_rent:.2f}"
)

# Identificar localidades (distritos) com quantidades consideráveis de registros:
districts = df['district'].value_counts()
FLOOR = 0.25 # Top 25% dos distritos
cutoff_count = districts.iloc[math.ceil(districts.size * FLOOR) - 1] # Resultará em 8
top_districts = districts.loc[districts >= cutoff_count].index

# Obter os distritos com o menor e maior preço médio, desde que tenham no mínimo 8 imóveis listados:
districts_mean_rent = (
    df.groupby('district')['rent']
    .agg(mean_rent='mean', n_records='count')
    .loc[top_districts]
    .sort_values('mean_rent', ascending=False)
    .reset_index() # Usa um índice numérico
    .rename(columns={
        'district': 'Localidade',
        'mean_rent': 'Aluguel médio (R$)',
        'n_records': 'Qtd. de registros',
    })
)

top_3_highest_rent = districts_mean_rent.head(3)
top_3_lowest_rent = districts_mean_rent.tail(3)[::-1].reset_index(drop=True)

print_section("Top 3 localidades com maior aluguel médio", top_3_highest_rent)
print_section("Top 3 localidades com menor aluguel médio", top_3_lowest_rent)

print('|==== FIM DO PROGRAMA ====|')

