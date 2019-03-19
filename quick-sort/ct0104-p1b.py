# Walmick Diógenes Nogueira de Queirós

#Gerar também séries invertidas de 200000 400000 600000 800000 e 1000000 de números e plotar o gráfico do tempo.

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

lista1 = sorted(list(range(20)), reverse=True)
lista2 = sorted(list(range(40)), reverse=True)
lista3 = sorted(list(range(60)), reverse=True)
lista4 = sorted(list(range(80)), reverse=True)
lista5 = sorted(list(range(100)), reverse=True)

geralista = [lista1, lista2, lista3, lista4, lista5]

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
    #varrido = list(i)
    varrer.append(timeit.timeit("quickSort({})".format(geralista), setup="from __main__ import quickSort", number=1))

print(quickSort(geralista))

desenhaGrafico(tamlista, varrer)
