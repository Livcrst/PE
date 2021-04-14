import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('brain_bodyweight.txt',delimiter="\t")

Brainweight = dados['Brainweight']
Bodyweight = dados['Bodyweight ']
Brainweight_SEM = dados['Brainweight.SEM']
Bodyweight_SEM = dados['Bodyweight.SEM']
Species  = dados['Species ']

fig, ax = plt.subplots(figsize=(6,6))

ax.errorbar(Brainweight, Bodyweight, xerr=Brainweight_SEM, yerr=Bodyweight_SEM,
             marker='o', markersize=2.5, color="k", capsize=3, linestyle='none')

plt.xlabel('Brain weight')
plt.ylabel('Body weight')

for i, label in enumerate(Species):
    ax.annotate(label, (Brainweight[i], Bodyweight[i]-0.3),size=6,ha='center')

plt.show()
