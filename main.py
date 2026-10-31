import pandas as pd

from scripts.pre_analysis import cleanse_df, print_df_stats
from scripts.user_interaction import ask_yes_no

df = pd.read_csv('data/Sao_Paulo_housing_prices_20230501.csv')

if ask_yes_no('Gostaria de verificar se os dados do dataset estão incoerentes? (S/n) \n--> '):
    print_df_stats(df)
    df = cleanse_df(df)

print('|==== FIM DO PROGRAMA ====|')

