import matplotlib.pyplot as plt #para plotar
import pandas as pd #Manipular os dados

arquivo = open('male_female_counts.txt')

def tratarDados(dados):
    #Percorrendo para salvar os dados do arquivo para salvar em listas e limpar o formato txt
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
testano = [ int(x) for x in testano] #Formata os dados para float

#Cria o gráfico
colors = ['red','orange','yellow','lime','springgreen','cyan','cornflowerblue','blue','violet','magenta'] #Define a cor para as colunas
dados = pd.DataFrame({'names': teste,'values': testano}) #Le dados a manipular
dados.plot('names','values',color=colors,ec='black',kind='bar') #Desenha o gráfico
plt.yticks([0,5,10,15]) #Coloca os limites do eixo y
plt.show()
