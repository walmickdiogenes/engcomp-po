#Walmick Diógenes Nogueira de Queirós

from random import randint
import matplotlib as mpl
import itertools as it
import timeit

permutacao = (list(it.permutations(range(6))))

'''def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista'''

def selection(lista):
    for i in range(0, len(lista) - 1):
        min = i
        for j in range(i + 1, len(lista)):
            if (lista[j] < lista[min]):
                min = j
        aux = lista[min]
        lista[min] = lista[i]
        lista[i] = aux
    return lista

tempo = []

for i in permutacao:
    permuta = list(i)
    tempo.append(timeit.timeit("selection({})".format(permuta),setup="from __main__ import selection",number=1))


melhorTempo = tempo.index(min(tempo))
piorTempo = tempo.index(max(tempo))

print(min(tempo))
print(permutacao[melhorTempo])
print(max(tempo))
print(permutacao[piorTempo])
