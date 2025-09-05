from itertools import product
K,M = map(int,input().split())
lista = []
for _ in range(K):
    datos = list(map(int, input().split()))
    lista.append(datos[1:])
combinaciones = []
for x in product(*lista):
    combinaciones.append(sum(n**2 for n in x) % M)

print(max(combinaciones))
    