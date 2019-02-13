from random import randint
import matplotlib as mpl
import itertools as it
import timeit

tamlista = (list(it.permutations(range(4))))

'''def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista'''

def selection(lista):
    for i in range(0, len(lista) - 1):
        min = i
        for j in range(i + 1, len(lista)):
            if (lista[j] < lista[min]):
                min = j
        aux = lista[min]
        lista[min] = lista[i]
        lista[i] = aux
    return lista

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
    fig.savefig('graph2.png')

