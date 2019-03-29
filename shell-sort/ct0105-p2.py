#Walmick Diógenes Nogueira de Queirós

#Mostrar qual realmente eh o pior caso para o algoritmo de seleção usando uma serie de 6 números
#(Gerar todas as permutações possíveis e mostrar o pior e o melhor resultados)

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

permutacao = (list(it.permutations(range(6))))

def shell_sort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            aux = array[i]
            j = i
            while j >= gap and array[j - gap] > aux:
                array[j] = array[j - gap]
                j -= gap
            array[j] = aux
        gap //= 2

        return(array)

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("shell_sort({})".format(permuta),setup="from __main__ import shell_sort",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
