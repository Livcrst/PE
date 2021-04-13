import pandas as pd
import matplotlib.pyplot as plt


dado = open('chromosome_position_data.txt')

def tratarDados(dados):
    #Percorrendo para salvar os dados do arquivo para 
    TratarDados = []
    for i in dados:
        dado = i.rstrip()
        TratarDados.append(dado)
    print('Fim')
    #Separa os valores pelo \t
    data =[]
    for j in TratarDados:
        valor = j.split('\t')
        dado = [ float(x) for x in valor]
        data.append(dado)
    print(data)
    positions = []
    mut1 = []
    mut2 = []
    wt = []
    for i in data:
        positions.append(i[0])
        mut1.append(i[1])
        mut2.append(i[2])
        wt.append(i[3])
    return positions,mut1,mut2,wt
pos,mut1,mut2,wt = tratarDados(dado)

plt.plot(pos,mut1,color='red',label='Mut1')
plt.plot(pos,mut2,color='blue',label='Mut2')
plt.plot(pos,wt,color='green',label='WT')
plt.xlabel('Position within chromosome')
plt.ylabel('value')
plt.legend()
plt.show()
