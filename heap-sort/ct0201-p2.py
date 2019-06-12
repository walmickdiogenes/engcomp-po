#Walmick Diógenes Nogueira de Queirós

#Mostrar qual realmente eh o pior caso para o algoritmo de seleção usando uma serie de 6 números
#(Gerar todas as permutações possíveis e mostrar o pior e o melhor resultados)

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

permutacao = (list(it.permutations(range(6))))

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

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("heapSort({})".format(permuta),setup="from __main__ import heapSort",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
