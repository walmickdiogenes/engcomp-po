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
   return alist

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("insertionSort({})".format(permuta),setup="from __main__ import insertionSort",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
