import matplotlib.pyplot as plt #para plotar

arquivo = open('feature_count.txt') #le o arquivo

def tratarDados(dados):
    #Percorrendo para salvar os dados do arquivo para salvar os dados 
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
        ex = valor[0]
        ey = float(valor[1])
        x.append(ex)
        y.append(ey)
    return x, y
teste,testano = tratarDados(arquivo)
#Cria a plotagem do grafico com barras horizontais
print(teste,testano)
plt.barh(teste,testano,color="gray")
plt.xlabel('Number of features')
plt.legend()
plt.show() 