# Walmick Diógenes Nogueira de Queirós

# Gerar séries invertidas de 200000 400000 600000 800000 e 1000000 de números e plotar o gráfico do tempo.

from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it
import timeit

lista1 = sorted(list(range(20)), reverse=True)
lista2 = sorted(list(range(40)), reverse=True)
lista3 = sorted(list(range(60)), reverse=True)
lista4 = sorted(list(range(80)), reverse=True)
lista5 = sorted(list(range(100)), reverse=True)

geralista = list[lista1, lista2, lista3, lista4, lista5]

def quickSort(listToSort):
    L = []
    R = []
    if len(listToSort) <= 1:
        return listToSort
    pivot = listToSort[len(listToSort) // 2]
    for i in listToSort:
        if i < pivot:
            L.append(i)
        if i > pivot:
            R.append(i)
    return quickSort(L) + [pivot] + quickSort(R)

mpl.use('Agg')
def desenhaGrafico(x, y, xl="Tamanho", yl="Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('casos2.png')

varrer = []

for i in geralista:
    varrer.append(timeit.timeit("quickSort({})".format(geralista), setup="from __main__ import quickSort", number=1))

print(quickSort(geralista))

#desenhaGrafico(geralista, varrer)
