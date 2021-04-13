import numpy as np
import matplotlib.pyplot as plt

# Questão 3
n_dist1 = np.random.normal(size=10000)
n_dist2 = np.random.normal(loc=4,size=10000)

n_dist = np.concatenate((n_dist1,n_dist2))

plt.figure(figsize=(12,5))
plt.hist(n_dist, bins=130, histtype='barstacked', color='white', ec='black')
plt.title("Mixed distribution histogram",fontweight="bold")
plt.xlabel("Values")
plt.yticks([0,100,200,300,400])
plt.ylabel("Frequency")

plt.show()