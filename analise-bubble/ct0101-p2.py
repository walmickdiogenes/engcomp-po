#Walmick Diógenes Nogueira de Queirós

from random import randint
import matplotlib as mpl
import timeit

tamlista = [1000, 2000, 3000, 4000, 5000]
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def bubbleSort(A):
  if len(A) <= 1:
      sA = A
  else:
      for j in range(0,len(A)):
          for i in range(0,len(A)-1):
              if A[i]>A[i+1]:
                  Aux = A[i+1]
                  A[i+1] = A[i]
                  A[i] = Aux
      sA = A

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

  melhorTempo.append(timeit.timeit("bubbleSort({})".format(melhor),setup="from __main__ import bubbleSort",number=1))
  piorTempo.append(timeit.timeit("bubbleSort({})".format(pior),setup="from __main__ import bubbleSort",number=1))
  medioTempo.append(timeit.timeit("bubbleSort({})".format(medio),setup="from __main__ import bubbleSort",number=1))



desenhaGrafico(tamlista,melhorTempo, piorTempo, medioTempo)