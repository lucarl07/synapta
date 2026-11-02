import math
import pandas as pd

from scripts.pre_analysis import cleanse_df, print_df_stats
from scripts.user_interaction import ask_yes_no, print_section
from scripts.utils import startsAt1Index

# ==:== Configurações do Pandas ==:==
pd.options.display.float_format = '{:.2f}'.format

# Ler DataFrame:
df = pd.read_csv('data/Sao_Paulo_housing_prices_20230501.csv')

# Verificação Pré-Limpeza (opcional):
if ask_yes_no(
    'Gostaria de verificar como estão os dados antes da limpeza? (s/N) \n--> ', 
    False
): print_df_stats(df)

# Limpeza obrigatória:
df = cleanse_df(df)

# Verificação Pós-Limpeza (opcional):
if ask_yes_no(
    'Gostaria de verificar como estão os dados após a limpeza? (s/N) \n--> ', 
    False
): print_df_stats(df)

print("") # Linha vazia, apenas para separar pré-análise da análise em si.

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
top_3_highest_rent.index = startsAt1Index(top_3_highest_rent)

top_3_lowest_rent = districts_mean_rent.tail(3)[::-1].reset_index(drop=True)
top_3_lowest_rent.index = startsAt1Index(top_3_lowest_rent)

print_section("Top 3 localidades com maior aluguel médio", top_3_highest_rent)
print_section("Top 3 localidades com menor aluguel médio", top_3_lowest_rent)

# Obter os imóveis com o maior valor de aluguel por metro quadrado de área:
rent_per_sm_df = (
    df.assign(rent_per_sm=lambda d: d['rent'] / d['area'])
      .sort_values(by='rent_per_sm', ascending=False)
      .reset_index()
      .drop(columns=['index', 'total'])
)

top_10_rent_per_sm = rent_per_sm_df.head(10).rename(columns={
    'address': 'Endereço',
    'district': 'Localidade',
    'area': 'Área (m²)',
    'bedrooms': 'Quartos',
    'garage': 'Vagas de estacionamento',
    'type': 'Tipo',
    'rent': 'Aluguel (R$)',
    'rent_per_sm': 'Aluguel por m²',
})
top_10_rent_per_sm.index = startsAt1Index(top_10_rent_per_sm)

print_section("Imóveis com maior aluguel por metro quadrado", str(top_10_rent_per_sm))

# ==:== FIM ==:== 
print('|==== FIM DO PROGRAMA ====|')

