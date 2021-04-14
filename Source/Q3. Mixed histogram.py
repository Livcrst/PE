import numpy as np
import matplotlib.pyplot as plt

# Questão 3

#Cria as distribuições normais com valores aleatorios
n_dist1 = np.random.normal(size=10000)
n_dist2 = np.random.normal(loc=4,size=10000) #Distribuição com deslocamento = 4

#Une as duas distribuições 
n_dist = np.concatenate((n_dist1,n_dist2))

#Cria gráfico histograma das normais com valores aleatorios
plt.figure(figsize=(12,5))
plt.hist(n_dist, bins=130, histtype='barstacked', color='white', ec='black')
plt.title("Mixed distribution histogram",fontweight="bold")
plt.xlabel("Values")
plt.yticks([0,100,200,300,400])
plt.ylabel("Frequency")

plt.show()