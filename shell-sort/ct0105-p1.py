#Walmick Diógenes Nogueira de Queirós
#Gerar series de 10000 a 50000 números e plotar gráficos com o melhor, médio e pior caso.

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

tamlista = [10000, 20000, 30000, 40000, 50000]
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def shell_sort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            aux = array[i]
            j = i
            while j >= gap and array[j - gap] > aux:
                array[j] = array[j - gap]
                j -= gap
            array[j] = aux
        gap //= 2

        return(array)

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
    fig.savefig('graph.png')

melhorTempo = []
piorTempo = []
medioTempo = []

for i in tamlista:
    medio = geraLista(i)
    melhor = sorted(medio)
    pior = sorted(medio, reverse=True)

    melhorTempo.append(timeit.timeit("shell_sort({})".format(melhor),setup="from __main__ import shell_sort",number=1))
    piorTempo.append(timeit.timeit("shell_sort({})".format(pior),setup="from __main__ import shell_sort",number=1))
    medioTempo.append(timeit.timeit("shell_sort({})".format(medio),setup="from __main__ import shell_sort",number=1))


desenhaGrafico(tamlista,melhorTempo, piorTempo, medioTempo)


