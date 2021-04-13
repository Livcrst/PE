import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('up_down_expression.txt',delimiter="\t")

unchanging = dados[dados.State == 'unchanging']
up = dados[dados.State == 'up']
down = dados[dados.State == 'down']

plt.figure(figsize=(6,6))
plt.scatter(unchanging.Condition1, unchanging.Condition2, color='silver', s=5.0)
plt.scatter(up.Condition1, up.Condition2, color='red', s=5.0)
plt.scatter(down.Condition1, down.Condition2, color='blue', s=5.0)
plt.xlabel('Condition 1')
plt.ylabel('Condition 2')
plt.xticks([0,5,10])
plt.yticks([0,5,10])
plt.legend(['unchanging','up','down'])
plt.show()