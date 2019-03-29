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

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    return alist

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
    fig.savefig('merge-graph.png')

melhorTempo = []
piorTempo = []
medioTempo = []

for i in tamlista:
  medio = geraLista(i)
  melhor = sorted(medio)
  pior = sorted(medio, reverse=True)

  melhorTempo.append(timeit.timeit("mergeSort({})".format(melhor), setup="from __main__ import mergeSort", number=1))
  piorTempo.append(timeit.timeit("mergeSort({})".format(pior), setup="from __main__ import mergeSort", number=1))
  medioTempo.append(timeit.timeit("mergeSort({})".format(medio), setup="from __main__ import mergeSort", number=1))

desenhaGrafico(tamlista, melhorTempo, piorTempo, medioTempo)

'''lista = [28, 5, 19, 98, 20]
print(mergeSort(lista))'''












