#Walmick Diógenes Nogueira de Queirós

#Mostrar qual realmente eh o pior caso para o algoritmo de seleção usando uma serie de 6 números
#(Gerar todas as permutações possíveis e mostrar o pior e o melhor resultados)

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

permutacao = (list(it.permutations(range(6))))

def insertionSort(alist):
   for i in range(1,len(alist)):
       current = alist[i]
       while i>0 and alist[i-1]>current:
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current

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

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("quickSort({})".format(permuta),setup="from __main__ import quickSort",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
