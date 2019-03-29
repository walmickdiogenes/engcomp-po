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

def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i] / size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])

    for i in range(length):
        insertionSort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("bucketSort({})".format(permuta),setup="from __main__ import bucketSort",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
