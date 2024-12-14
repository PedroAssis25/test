

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns



df = pd.read_csv('gasolina.csv')

sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))

sns.lineplot(x='dia', y='venda', data=df, marker='o')

plt.title('Preço da Gasolina por Dia', fontsize=14)

plt.xlabel('Dia', fontsize=12)

plt.ylabel('Preço (R$)', fontsize=12)

plt.tight_layout()

plt.savefig('gasolina.png')

plt.show()

