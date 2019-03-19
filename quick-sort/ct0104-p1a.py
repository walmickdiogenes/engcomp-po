# Walmick Diógenes Nogueira de Queirós

#Gerar series de 10000 a 50000 números e plotar gráficos com o melhor, médio e pior caso.

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

tamlista = [10, 20, 30, 40, 50]

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1, 1 * tam)
        if n not in lista: lista.append(n)
    return lista


def quickSort(listToSort):
    # low and high lists
    L = []
    R = []
    # if the list has less than one element, return it
    if len(listToSort) <= 1:
        return listToSort
    # the pivot is a number in the list middle
    pivot = listToSort[len(listToSort) // 2]
    for i in listToSort:
        # append the smaller numbers in the left array
        if i < pivot:
            L.append(i)
        # append the higher numbers in the right array
        if i > pivot:
            R.append(i)
    # the sorted list is the left + pivot + right numbers
    return quickSort(L) + [pivot] + quickSort(R)


mpl.use('Agg')
import matplotlib.pyplot as plt


def desenhaGrafico(x, y, ym, yp, xl="Tamanho", yl="Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.plot(x, ym, label="Medio Tempo")
    ax.plot(x, yp, label="Pior Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('casos.png')


melhorTempo = []
piorTempo = []
medioTempo = []

for i in tamlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(medio, reverse=True)

    melhorTempo.append(timeit.timeit("quickSort({})".format(melhor), setup="from __main__ import quickSort", number=1))
    piorTempo.append(timeit.timeit("quickSort({})".format(pior), setup="from __main__ import quickSort", number=1))
    medioTempo.append(timeit.timeit("quickSort({})".format(medio), setup="from __main__ import quickSort", number=1))


desenhaGrafico(tamlista, melhorTempo, piorTempo, medioTempo)
