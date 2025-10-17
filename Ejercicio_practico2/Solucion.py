"""
📋 Ejercicio B1: Filtrado de listas
Descripción: Escribe una función que filtre los números pares de una lista.
"""

def filtrado_listas(lista)->list:
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares
"""
📋 Ejercicio B2: Invertir diccionario
Descripción: Escribe una función que invierta las claves 
y valores de un diccionario (asumiendo valores únicos).
"""
def reverse_dict(dicc: dict):
    reverse_d = {}
    for key,value in dicc.items():
        reverse_d[value] = key
    return reverse_d

"""
📋 Ejercicio B3: Elementos comunes en dos listas
Descripción: Encuentra los elementos comunes entre dos listas, sin duplicados.
"""

def comunes(l1,l2)->list:
    return [n for n in l1 if n in l2]

"""
📋 Ejercicio B4: Contador de palabras
Descripción: Escribe una función que cuente la frecuencia de cada palabra en una cadena.
"""

def contador_palabras(cadena: str):
    contador = {}
    for palabra in cadena.split(" "):
        contador[palabra] = contador.get(palabra,0) + 1
    return contador

"""
📋 Ejercicio B5: Eliminar duplicados manteniendo orden
"""

def eliminar_duplicados(lista:list):
    return list(set(lista))

"""
📋 Ejercicio I1: Agrupar por atributo
Descripción: Escribe una función que agrupe objetos por un atributo específico.
"""

def agrupar_atributos(dics: list,atributo:str):
    agrupar = {}
    for dic in dics:
        agrupar[dic[atributo]] = [est for est in dics if dic[atributo] == est[atributo]]
    return agrupar

"""
📋 Ejercicio I2: Fusionar diccionarios anidados
Descripción: Fusiona dos diccionarios anidados, combinando los valores cuando las claves coincidan.
"""

def fusion_dic(d1, d2):
    resultado = d1.copy()
    for clave, valor in d2.items():
        if clave in resultado and isinstance(resultado[clave], dict) and isinstance(valor, dict):
            resultado[clave] = fusion_dic(resultado[clave], valor)
        else:
            resultado[clave] = valor
    return resultado


# I3
def par_suma(numeros, objetivo):
    vistos = set()
    for n in numeros:
        if objetivo - n in vistos:
            return (objetivo - n, n)
        vistos.add(n)
    return None


# I4
def transponer(matriz):
    return [list(fila) for fila in zip(*matriz)]


# I5
def contar_categoria(datos):
    conteo = {}
    for categoria, elemento in datos:
        if categoria not in conteo:
            conteo[categoria] = set()
        conteo[categoria].add(elemento)
    return {k: len(v) for k, v in conteo.items()}


# A1
def fibonacci(n):
    memo = {}
    def f(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            res = k
        else:
            res = f(k-1) + f(k-2)
        memo[k] = res
        return res
    return f(n)


# A2
class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = {}
        self.orden = []

    def get(self, clave):
        if clave not in self.cache:
            return None
        self.orden.remove(clave)
        self.orden.append(clave)
        return self.cache[clave]

    def put(self, clave, valor):
        if clave in self.cache:
            self.orden.remove(clave)
        elif len(self.cache) >= self.capacidad:
            viejo = self.orden.pop(0)
            del self.cache[viejo]
        self.cache[clave] = valor
        self.orden.append(clave)


# A3
class MiConjunto:
    def __init__(self):
        self.elementos = []

    def add(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def remove(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
        else:
            raise KeyError(f"{elemento} no está en el conjunto")

    def discard(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def __contains__(self, elemento):
        return elemento in self.elementos

    def __len__(self):
        return len(self.elementos)

    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"


# A4
def filtrar_jugadores(datos, condicion):
    resultado = {}
    for equipo, info in datos.items():
        resultado[equipo] = {"jugadores": []}
        for jugador in info.get("jugadores", []):
            if condicion(jugador):
                resultado[equipo]["jugadores"].append(jugador)
    return resultado


# A5
def buscar_ruta(arbol, valor):
    def recorrer(nodo, camino):
        if not nodo:
            return None
        camino.append(nodo["valor"])
        if nodo["valor"] == valor:
            return camino
        izq = recorrer(nodo.get("izquierdo"), camino.copy())
        if izq:
            return izq
        der = recorrer(nodo.get("derecho"), camino.copy())
        if der:
            return der
        return None
    return recorrer(arbol, [])
