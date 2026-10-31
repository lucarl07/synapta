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
print_section("Valores", f"Média dos aluguéis: {mean_rent} \nMediana dos aluguéis: {median_rent}")

print('|==== FIM DO PROGRAMA ====|')

