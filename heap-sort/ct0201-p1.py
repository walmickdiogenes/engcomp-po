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

def heapSort(listToSort):
  for start in range((len(listToSort)-2)//2, -1, -1):
    siftdown(listToSort, start, len(listToSort)-1)

  for end in range(len(listToSort)-1, 0, -1):
    listToSort[end], listToSort[0] = listToSort[0], listToSort[end]
    siftdown(listToSort, 0, end - 1)
  return listToSort

def siftdown(listToSort, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and listToSort[child] < listToSort[child + 1]:
      child += 1
    if listToSort[root] < listToSort[child]:
      listToSort[root], listToSort[child] = listToSort[child], listToSort[root]
      root = child
    else:
      break

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

  melhorTempo.append(timeit.timeit("heapSort({})".format(melhor),setup="from __main__ import heapSort",number=1))
  piorTempo.append(timeit.timeit("heapSort({})".format(pior),setup="from __main__ import heapSort",number=1))
  medioTempo.append(timeit.timeit("heapSort({})".format(medio),setup="from __main__ import heapSort",number=1))

desenhaGrafico(tamlista,melhorTempo, piorTempo, medioTempo)