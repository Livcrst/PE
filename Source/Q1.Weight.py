import matplotlib.pyplot as plt #para plotar
dados = open('weight_chart.txt','r')

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
        ex = int(valor[0])
        ey = float(valor[1])
        x.append(ex)
        y.append(ey)
    return x, y
teste,testano = tratarDados(dados)

print(teste,testano)
plt.plot(teste,testano, marker="o",color="black")
plt.xlabel('Age (months)')
plt.ylabel('Weight (kg)')
plt.legend()
plt.title("The relationship between age and weight in a growing infant")
plt.show()