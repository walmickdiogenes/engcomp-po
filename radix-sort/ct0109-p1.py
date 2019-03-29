#Walmick Diógenes Nogueira de Queirós

#Gerar series de 10000 a 50000 números e plotar gráficos com o melhor, médio e pior caso.

from random import randint
import matplotlib as mpl
import timeit

tamlista = [10000, 20000, 30000, 40000, 50000]

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista


def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[(index) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
    return arr

mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,ym,yp,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.plot(x,ym, label = "Medio Tempo")
    ax.plot(x,yp, label = "Pior Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('radix-graph.png')

melhorTempo = []
piorTempo = []
medioTempo = []

for i in tamlista:
  medio = geraLista(i)
  melhor = sorted(medio)
  pior = sorted(medio, reverse=True)

  melhorTempo.append(timeit.timeit("radixSort({})".format(melhor),setup="from __main__ import radixSort",number=1))
  piorTempo.append(timeit.timeit("radixSort({})".format(pior),setup="from __main__ import radixSort",number=1))
  medioTempo.append(timeit.timeit("radixSort({})".format(medio),setup="from __main__ import radixSort",number=1))

desenhaGrafico(tamlista,melhorTempo, piorTempo, medioTempo)