import matplotlib.pyplot as plt #para plotar
import pandas as pd

arquivo = open('male_female_counts.txt')

def tratarDados(dados):
    #Percorrendo para salvar os dados do arquivo para 
    TratarDados = []
    for i in dados:
        dado = i.rstrip()
        TratarDados.append(dado)
    print('Fim')
    #Separa os valores pelo \t
    x = []
    y = []
    for j in TratarDados:
        valor = j.split('\t')
        print(valor)
        ex,ey = valor[0].split(' ')
        print(ex,ey)
        x.append(ex)
        y.append(ey)
    return x, y
teste,testano = tratarDados(arquivo)
testano = [ int(x) for x in testano]


colors = ['red','orange','yellow','lime','springgreen','cyan','cornflowerblue','blue','violet','magenta']
dados = pd.DataFrame({'names': teste,'values': testano})
dados.plot('names','values',color=colors,ec='black',kind='bar')
plt.yticks([0,5,10,15])
plt.show()
