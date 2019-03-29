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

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("mergeSort({})".format(permuta),setup="from __main__ import mergeSort",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
