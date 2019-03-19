# Walmick Diógenes Nogueira de Queirós

# 1. GERAR SÉRIES ALEATÓRIAS COM AS SEGUINTES QUANTIDADES DE NÚMEROS: 10000, 20000, 30000, 40000 E 50000
# 2. CALCULAR O TEMPO E NÚMERO DE COMPARAÇÕES REALIZADAS PARA ORDENAR ESTAS SÉRIES PELO MÉTODO DA BOLHA
# 3. PLOTAR GRÁFICOS COMPARATIVOS PARA AMBOS OS CASOS.


from random import randint
import matplotlib as mpl
import timeit

tamlista = [10, 20, 30, 40, 50]
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def bubbleSort(A):
  trocas = 0
  if len(A) <= 1:
      sA = A
  else:
      for j in range(0,len(A)):
          for i in range(0,len(A)-1):
              if A[i]>A[i+1]:
                  Aux = A[i+1]
                  A[i+1] = A[i]
                  A[i] = Aux
                  trocas += 1
      sA = A

  return trocas

mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y,xl = "Tamanho", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')

tempos = []
trocas = []

for i in tamlista:
  lista = geraLista(i)
  trocas.append(bubbleSort(lista))
  tempo = timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1)
  tempos.append(tempo)

desenhaGrafico(tamlista,tempos)
#desenhaGrafico(tamlista,trocas)