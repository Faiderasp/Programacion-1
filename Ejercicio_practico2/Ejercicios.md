Ejercicios Prácticos: Estructuras de Datos en Python
📝 Instrucciones
Este documento contiene ejercicios prácticos para fortalecer tu comprensión de las estructuras de datos en Python. Cada ejercicio incluye:

Descripción del problema
Ejemplo de entrada/salida esperada
Consejos para resolverlo
Solución (como referencia, ¡intenta resolverlo primero por tu cuenta!)
Los ejercicios están organizados por nivel de dificultad (básico, intermedio y avanzado) y por tipo de estructura de datos.

Nivel Básico
📋 Ejercicio B1: Filtrado de listas
Descripción: Escribe una función que filtre los números pares de una lista.

Ejemplo:

>>> filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
[2, 4, 6, 8, 10]
Consejos: - Usa la operación módulo (%) para verificar si un número es par - Puedes usar una comprensión de lista

Solución:

def filtrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0]
📋 Ejercicio B2: Invertir diccionario
Descripción: Escribe una función que invierta las claves y valores de un diccionario (asumiendo valores únicos).

Ejemplo:

>>> invertir_diccionario({"a": 1, "b": 2, "c": 3})
{1: "a", 2: "b", 3: "c"}
Consejos: - Recorre el diccionario usando .items() - Crea un nuevo diccionario con las claves y valores intercambiados

Solución:

def invertir_diccionario(diccionario):
    return {valor: clave for clave, valor in diccionario.items()}
📋 Ejercicio B3: Elementos comunes en dos listas
Descripción: Encuentra los elementos comunes entre dos listas, sin duplicados.

Ejemplo:

>>> elementos_comunes([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
[4, 5]
Consejos: - Convierte las listas en conjuntos - Usa la operación de intersección de conjuntos (&)

Solución:

def elementos_comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))
📋 Ejercicio B4: Contador de palabras
Descripción: Escribe una función que cuente la frecuencia de cada palabra en una cadena.

Ejemplo:

>>> contar_palabras("hola mundo hola python")
{"hola": 2, "mundo": 1, "python": 1}
Consejos: - Divide la cadena en palabras con split() - Usa un diccionario para contar ocurrencias

Solución:

def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador
📋 Ejercicio B5: Eliminar duplicados manteniendo orden
Descripción: Elimina duplicados de una lista manteniendo el orden original.

Ejemplo:

>>> eliminar_duplicados([1, 2, 2, 3, 4, 3, 5])
[1, 2, 3, 4, 5]
Consejos: - No uses simplemente list(set(lista)) porque altera el orden - Usa un diccionario para mantener el orden (Python 3.7+)

Solución:

def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))
Nivel Intermedio
📋 Ejercicio I1: Agrupar por atributo
Descripción: Escribe una función que agrupe objetos por un atributo específico.

Ejemplo:

estudiantes = [
    {"nombre": "Ana", "ciudad": "Madrid"},
    {"nombre": "Juan", "ciudad": "Barcelona"},
    {"nombre": "Maria", "ciudad": "Madrid"},
    {"nombre": "Pedro", "ciudad": "Valencia"}
]

>>> agrupar_por(estudiantes, "ciudad")
{
    "Madrid": [{"nombre": "Ana", "ciudad": "Madrid"}, {"nombre": "Maria", "ciudad": "Madrid"}],
    "Barcelona": [{"nombre": "Juan", "ciudad": "Barcelona"}],
    "Valencia": [{"nombre": "Pedro", "ciudad": "Valencia"}]
}
Consejos: - Usa un diccionario con listas como valores - Comprueba si la clave existe antes de añadir

Solución:

def agrupar_por(objetos, atributo):
    resultado = {}
    for obj in objetos:
        valor = obj[atributo]
        if valor not in resultado:
            resultado[valor] = []
        resultado[valor].append(obj)
    return resultado

# Alternativa con defaultdict
from collections import defaultdict

def agrupar_por_alt(objetos, atributo):
    resultado = defaultdict(list)
    for obj in objetos:
        resultado[obj[atributo]].append(obj)
    return dict(resultado)
📋 Ejercicio I2: Fusionar diccionarios anidados
Descripción: Fusiona dos diccionarios anidados, combinando los valores cuando las claves coincidan.

Ejemplo:

dict1 = {"a": 1, "b": {"x": 10, "y": 20}}
dict2 = {"c": 3, "b": {"y": 30, "z": 40}}

>>> fusionar_diccionarios(dict1, dict2)
{"a": 1, "c": 3, "b": {"x": 10, "y": 30, "z": 40}}
Consejos: - Maneja el caso especial cuando ambos valores son diccionarios - Usa recursividad para manejar la anidación

Solución:

def fusionar_diccionarios(dict1, dict2):
    resultado = dict1.copy()
    
    for clave, valor in dict2.items():
        if clave in resultado and isinstance(resultado[clave], dict) and isinstance(valor, dict):
            resultado[clave] = fusionar_diccionarios(resultado[clave], valor)
        else:
            resultado[clave] = valor
            
    return resultado
📋 Ejercicio I3: Encontrar el par que suma
Descripción: Dada una lista de números y un valor objetivo, encuentra un par de números que sumen ese valor.

Ejemplo:

>>> encontrar_par_suma([1, 5, 3, 7, 9, 2], 10)
(1, 9)  # o (3, 7)
Consejos: - Usa un conjunto para buscar complementos - Para cada número n, verifica si objetivo - n ya fue visto

Solución:

def encontrar_par_suma(numeros, objetivo):
    vistos = set()
    for num in numeros:
        complemento = objetivo - num
        if complemento in vistos:
            return (complemento, num)
        vistos.add(num)
    return None
📋 Ejercicio I4: Matriz como lista de listas
Descripción: Transponer una matriz representada como lista de listas.

Ejemplo:

>>> transponer([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Consejos: - Usa zip(*matriz) o comprensión de listas anidadas - Asegúrate de que todas las filas tengan la misma longitud

Solución:

def transponer(matriz):
    return [list(fila) for fila in zip(*matriz)]

# Alternativa con comprensión de listas anidada
def transponer_alt(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
📋 Ejercicio I5: Contar elementos únicos por categoría
Descripción: Cuenta elementos únicos por categoría dada una lista de tuplas (categoría, elemento).

Ejemplo:

datos = [
    ("fruta", "manzana"),
    ("verdura", "zanahoria"),
    ("fruta", "plátano"),
    ("fruta", "manzana"),
    ("verdura", "lechuga")
]

>>> contar_por_categoria(datos)
{"fruta": 2, "verdura": 2}  # 2 frutas únicas, 2 verduras únicas
Consejos: - Usa un diccionario con conjuntos como valores - Convierte a conjunto para obtener elementos únicos

Solución:

def contar_por_categoria(datos):
    categorias = {}
    for categoria, elemento in datos:
        if categoria not in categorias:
            categorias[categoria] = set()
        categorias[categoria].add(elemento)
    
    return {categoria: len(elementos) for categoria, elementos in categorias.items()}
Nivel Avanzado
📋 Ejercicio A1: Memoización con diccionario
Descripción: Implementa una función para calcular números de Fibonacci usando memoización.

Ejemplo:

>>> fib(10)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
55
Consejos: - Usa un diccionario para almacenar resultados ya calculados - Define una función auxiliar recursiva

Solución:

def fibonacci(n):
    memoria = {}
    
    def fib_memo(n):
        if n in memoria:
            return memoria[n]
        
        if n <= 1:
            resultado = n
        else:
            resultado = fib_memo(n - 1) + fib_memo(n - 2)
            
        memoria[n] = resultado
        return resultado
    
    return fib_memo(n)
📋 Ejercicio A2: Sistema de caché LRU
Descripción: Implementa una caché que elimine el elemento menos recientemente usado (LRU) cuando alcanza su capacidad.

Ejemplo:

cache = LRUCache(2)  # capacidad 2
cache.put(1, "uno")
cache.put(2, "dos")
cache.get(1)         # "uno"
cache.put(3, "tres") # elimina la clave 2
cache.get(2)         # None
Consejos: - Usa un diccionario para almacenar valores - Usa una estructura auxiliar para mantener el orden de uso

Solución:

class LRUCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = {}
        self.orden_uso = []
        
    def get(self, clave):
        if clave not in self.cache:
            return None
        
        # Actualizar orden de uso
        self.orden_uso.remove(clave)
        self.orden_uso.append(clave)
        
        return self.cache[clave]
        
    def put(self, clave, valor):
        # Si la clave ya existe, actualizar su orden de uso
        if clave in self.cache:
            self.orden_uso.remove(clave)
        # Si está llena la caché, eliminar el menos usado
        elif len(self.cache) >= self.capacidad:
            clave_antigua = self.orden_uso.pop(0)
            del self.cache[clave_antigua]
            
        # Agregar nuevo elemento
        self.cache[clave] = valor
        self.orden_uso.append(clave)
📋 Ejercicio A3: Implementar conjunto con lista
Descripción: Implementa tu propia clase Set usando una lista como estructura de datos subyacente.

Ejemplo:

mi_conjunto = MiConjunto()
mi_conjunto.add(1)
mi_conjunto.add(2)
mi_conjunto.add(1)  # No añade duplicados
print(len(mi_conjunto))  # 2
print(1 in mi_conjunto)  # True
Consejos: - Usa una lista interna para almacenar elementos - Verifica si el elemento ya existe antes de añadirlo

Solución:

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
📋 Ejercicio A4: Filtrado de datos anidados
Descripción: Filtra elementos en una estructura anidada basada en una condición.

Ejemplo:

datos = {
    "equipo1": {"jugadores": [{"nombre": "Ana", "puntos": 120}, {"nombre": "Juan", "puntos": 80}]},
    "equipo2": {"jugadores": [{"nombre": "Maria", "puntos": 90}, {"nombre": "Pedro", "puntos": 150}]}
}

>>> filtrar_jugadores(datos, lambda j: j["puntos"] > 100)
{
    "equipo1": {"jugadores": [{"nombre": "Ana", "puntos": 120}]},
    "equipo2": {"jugadores": [{"nombre": "Pedro", "puntos": 150}]}
}
Consejos: - Usa recursividad para navegar la estructura - Aplica la función de filtrado solo a los jugadores

Solución:

def filtrar_jugadores(datos, condicion):
    resultado = {}
    
    for equipo, info in datos.items():
        resultado[equipo] = {"jugadores": []}
        
        for jugador in info["jugadores"]:
            if condicion(jugador):
                resultado[equipo]["jugadores"].append(jugador)
                
    return resultado
📋 Ejercicio A5: Operaciones sobre árboles (diccionarios anidados)
Descripción: Implementa una función que encuentre la ruta a un nodo en un árbol representado como diccionario anidado.

Ejemplo:

arbol = {
    "valor": "A",
    "izquierdo": {
        "valor": "B",
        "izquierdo": {"valor": "D", "izquierdo": None, "derecho": None},
        "derecho": {"valor": "E", "izquierdo": None, "derecho": None}
    },
    "derecho": {
        "valor": "C",
        "izquierdo": None,
        "derecho": {"valor": "F", "izquierdo": None, "derecho": None}
    }
}

>>> encontrar_ruta(arbol, "F")
["A", "C", "F"]
Consejos: - Usa recursividad para explorar el árbol - Devuelve la ruta cuando encuentres el valor buscado

Solución:

def encontrar_ruta(arbol, valor):
    def buscar(nodo, camino_actual):
        if nodo is None:
            return None
        
        camino_actual.append(nodo["valor"])
        
        if nodo["valor"] == valor:
            return camino_actual
            
        # Buscar en subárbol izquierdo
        camino_izq = buscar(nodo["izquierdo"], camino_actual.copy())
        if camino_izq:
            return camino_izq
            
        # Buscar en subárbol derecho
        camino_der = buscar(nodo["derecho"], camino_actual.copy())
        if camino_der:
            return camino_der
            
        return None
    
    return buscar(arbol, [])
Ejercicios de Depuración
🐞 Depuración 1: Modificación no intencionada
Código con error:

def agregar_puntos(equipos, equipo, puntos):
    equipos[equipo] = puntos
    return equipos

puntuacion = {"Equipo A": 10, "Equipo B": 15}
nuevos = agregar_puntos(puntuacion, "Equipo C", 12)

print(puntuacion)  # {"Equipo A": 10, "Equipo B": 15, "Equipo C": 12}
print(nuevos)      # {"Equipo A": 10, "Equipo B": 15, "Equipo C": 12}
Problema: La función modifica el diccionario original porque los diccionarios se pasan por referencia.

Solución:

def agregar_puntos(equipos, equipo, puntos):
    resultado = equipos.copy()  # Crear copia
    resultado[equipo] = puntos
    return resultado
🐞 Depuración 2: Referencia circular en JSON
Código con error:

import json

# Crear estructura con referencia circular
a = {"nombre": "objeto a"}
b = {"nombre": "objeto b", "referencia": a}
a["referencia"] = b

# Intenta convertirlo a JSON
json_str = json.dumps(a)
Problema: json.dumps() no puede serializar estructuras con referencias circulares.

Solución:

import json

class ReferenceResolver:
    def __init__(self):
        self.memo = {}
        self.counter = 0
        
    def __call__(self, obj):
        if isinstance(obj, dict):
            obj_id = id(obj)
            if obj_id in self.memo:
                return {"$ref": self.memo[obj_id]}
            
            self.counter += 1
            ref_id = f"id{self.counter}"
            self.memo[obj_id] = ref_id
            
            result = {"$id": ref_id}
            for k, v in obj.items():
                result[k] = self(v)
            return result
        return obj

# Crear estructura con referencia circular
a = {"nombre": "objeto a"}
b = {"nombre": "objeto b", "referencia": a}
a["referencia"] = b

# Serializar con referencia
json_str = json.dumps(a, default=ReferenceResolver())
print(json_str)
🐞 Depuración 3: Modificación durante iteración
Código con error:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Eliminar números pares
for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)
        
print(numeros)  # [1, 3, 5, 7, 9, 10]  ¿Por qué quedó el 10?
Problema: Al modificar la lista durante la iteración, se salta elementos porque los índices cambian.

Solución:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solución 1: Usar list comprehension
numeros = [x for x in numeros if x % 2 != 0]

# Solución 2: Iterar sobre una copia
for numero in numeros[:]:  # La notación [:] crea una copia
    if numero % 2 == 0:
        numeros.remove(numero)

# Solución 3: Iterar en reversa
for i in range(len(numeros) - 1, -1, -1):
    if numeros[i] % 2 == 0:
        numeros.pop(i)
Proyecto Integrador
📊 Sistema de Análisis de Datos de Ventas
Descripción: Desarrolla un sistema que analice datos de ventas para una tienda, utilizando diferentes estructuras de datos para almacenar, filtrar y calcular estadísticas.

Requisitos: 1. Cargar datos de ventas desde un archivo (puedes crearlo como diccionario) 2. Agrupar ventas por categoría, mes y vendedor 3. Encontrar los productos más vendidos 4. Calcular estadísticas como ventas totales, promedio y mediana 5. Implementar búsquedas eficientes por diferentes criterios

Datos de ejemplo:

ventas = [
    {"id": 1, "producto": "Laptop", "categoria": "Electrónica", "precio": 1200, "fecha": "2023-01-15", "vendedor": "Ana"},
    {"id": 2, "producto": "Monitor", "categoria": "Electrónica", "precio": 200, "fecha": "2023-01-20", "vendedor": "Juan"},
    {"id": 3, "producto": "Teclado", "categoria": "Accesorios", "precio": 80, "fecha": "2023-02-05", "vendedor": "Ana"},
    {"id": 4, "producto": "Mouse", "categoria": "Accesorios", "precio": 25, "fecha": "2023-02-10", "vendedor": "Pedro"},
    {"id": 5, "producto": "Laptop", "categoria": "Electrónica", "precio": 1500, "fecha": "2023-02-15", "vendedor": "Juan"},
    {"id": 6, "producto": "Teléfono", "categoria": "Electrónica", "precio": 800, "fecha": "2023-03-05", "vendedor": "Ana"},
    {"id": 7, "producto": "Tablet", "categoria": "Electrónica", "precio": 300, "fecha": "2023-03-10", "vendedor": "Pedro"},
    {"id": 8, "producto": "Teclado", "categoria": "Accesorios", "precio": 85, "fecha": "2023-03-15", "vendedor": "Juan"},
    {"id": 9, "producto": "Monitor", "categoria": "Electrónica", "precio": 250, "fecha": "2023-04-05", "vendedor": "Ana"},
    {"id": 10, "producto": "Mouse", "categoria": "Accesorios", "precio": 30, "fecha": "2023-04-10", "vendedor": "Pedro"}
]
Solución parcial:

from collections import defaultdict
from datetime import datetime
import statistics

class AnalizadorVentas:
    def __init__(self, datos_ventas):
        self.ventas = datos_ventas
        self.ventas_por_categoria = self._agrupar_por("categoria")
        self.ventas_por_mes = self._agrupar_por_mes()
        self.ventas_por_vendedor = self._agrupar_por("vendedor")
        self.productos_vendidos = self._contar_productos()
        
    def _agrupar_por(self, campo):
        """Agrupa ventas por un campo específico"""
        resultado = defaultdict(list)
        for venta in self.ventas:
            resultado[venta[campo]].append(venta)
        return dict(resultado)
    
    def _agrupar_por_mes(self):
        """Agrupa ventas por mes"""
        resultado = defaultdict(list)
        for venta in self.ventas:
            fecha = datetime.strptime(venta["fecha"], "%Y-%m-%d")
            mes = f"{fecha.year}-{fecha.month:02d}"
            resultado[mes].append(venta)
        return dict(resultado)
    
    def _contar_productos(self):
        """Cuenta la frecuencia de cada producto vendido"""
        contador = {}
        for venta in self.ventas:
            producto = venta["producto"]
            contador[producto] = contador.get(producto, 0) + 1
        return contador
    
    def productos_mas_vendidos(self, n=3):
        """Retorna los N productos más vendidos"""
        return sorted(self.productos_vendidos.items(), 
                     key=lambda x: x[1], reverse=True)[:n]
    
    def total_ventas_por_categoria(self):
        """Calcula el total de ventas por categoría"""
        resultado = {}
        for categoria, ventas in self.ventas_por_categoria.items():
            resultado[categoria] = sum(v["precio"] for v in ventas)
        return resultado
    
    def estadisticas_vendedor(self, vendedor):
        """Calcula estadísticas para un vendedor específico"""
        if vendedor not in self.ventas_por_vendedor:
            return None
        
        ventas = self.ventas_por_vendedor[vendedor]
        precios = [v["precio"] for v in ventas]
        
        return {
            "total": sum(precios),
            "promedio": statistics.mean(precios),
            "mediana": statistics.median(precios),
            "cantidad": len(precios),
            "min": min(precios),
            "max": max(precios)
        }
    
    def buscar_ventas(self, **criterios):
        """Busca ventas que cumplan con todos los criterios especificados"""
        resultado = []
        
        for venta in self.ventas:
            cumple = True
            for campo, valor in criterios.items():
                if campo not in venta or venta[campo] != valor:
                    cumple = False
                    break
            
            if cumple:
                resultado.append(venta)
                
        return resultado

# Ejemplo de uso
analizador = AnalizadorVentas(ventas)
print("Productos más vendidos:", analizador.productos_mas_vendidos(2))
print("Total por categoría:", analizador.total_ventas_por_categoria())
print("Estadísticas de Ana:", analizador.estadisticas_vendedor("Ana"))
print("Búsqueda:", analizador.buscar_ventas(categoria="Accesorios", vendedor="Juan"))
Desafío adicional: - Implementa una funcionalidad para buscar ventas en un rango de fechas - Añade un índice invertido para búsquedas más eficientes por múltiples campos - Crea visualizaciones de los datos (usando matplotlib si está disponible)

Conclusión
Estos ejercicios están diseñados para ayudarte a dominar el uso de las diferentes estructuras de datos en Python y comprender cuándo usar cada una. Algunas recomendaciones finales:

Práctica constante: Resuelve los ejercicios sin mirar las soluciones primero
Experimenta: Intenta soluciones alternativas y compara su eficiencia
Analiza la complejidad: Piensa en términos de O(n) para cada operación
Reutiliza y combina: Las estructuras de datos a menudo funcionan mejor juntas
Si tienes dudas o necesitas ayuda, consulta la guía de referencia o pregunta a tu profesor. ¡Buena suerte!

Este documento fue preparado como parte del material didáctico para el curso de Programación Orientada a Objetos.