import pandas as pd

df = pd.read_csv("data/glycemie.csv")

df

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

for time in df.columns[1:]:  # Colonnes de points de mesure par slicing

    if not 'AUCUN' in time:

        plt.plot(df.index, df[time], label=str(time))

        plt.xticks(rotation=45)
        plt.ylabel('Glycémie (g/l)', size=14)
        plt.xlabel('Date', size=14)
        plt.legend()
