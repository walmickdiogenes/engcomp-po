#Walmick Diógenes Nogueira de Queirós

#Mostrar qual realmente eh o pior caso para o algoritmo de seleção usando uma serie de 6 números
#(Gerar todas as permutações possíveis e mostrar o pior e o melhor resultados)

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

permutacao = (list(it.permutations(range(6))))

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[(index) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
    return arr

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("radixSort({})".format(permuta),setup="from __main__ import radixSort",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
