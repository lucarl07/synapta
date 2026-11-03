import matplotlib.pyplot as plt

from pandas import DataFrame

def plot_rent_histogram(df: DataFrame, media, mediana):
    rent = df['rent']
    rent_clipped = rent.filter(cond=rent <= rent.quantile(0.99))

    fig, ax = plt.subplots()
    rent_clipped.plot.hist(bins=70)

    ax.set_title('Distribuição dos aluguéis')
    ax.axvline(media, color='red', linestyle='--', label='Média')
    ax.axvline(mediana, color='#c9b44b', linestyle='--', label='Mediana')
    ax.set_xlabel('Aluguel (R$)')
    ax.set_ylabel('Frequência')
    ax.legend()

    # Texto de observação:
    plt.figtext(
        0.5, 0.01,
        'Observação: média e mediana calculadas com todos os dados, enquanto o gráfico exclui o 1% de valores mais altos.',
        ha='center', fontsize=8,
    )
    plt.tight_layout(rect=(0, 0.04, 1, 1)) 

    return fig

def plot_rent_per_sm_median_per_bedrooms(df: DataFrame):
    fig, ax = plt.subplots()
    df.groupby('bedrooms')['rent_per_sm'].median().plot.bar()

    ax.set_xlabel('Quartos')
    ax.set_ylabel('Mediana do aluguel por m² (R$)')
    ax.set_title('Aluguel por m² por número de quartos')
    ax.tick_params(axis='x', rotation=0)

    return fig

def plot_rent_per_sm_median_per_parking_spots(df: DataFrame):
    fig, ax = plt.subplots()
    df.groupby('garage')['rent_per_sm'].median().plot.bar()

    ax.set_xlabel('Vagas de estacionamento')
    ax.set_ylabel('Mediana do aluguel por m² (R$)')
    ax.set_title('Aluguel por m² por número de vagas de estacionamento')
    ax.tick_params(axis='x', rotation=0)

    return fig

