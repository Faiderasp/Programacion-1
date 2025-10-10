"""
OPERADORES LÓGICOS CONFUSOS - Actividad 1
Este código demuestra errores comunes y confusión con operadores lógicos en Python.
Los estudiantes deben identificar los problemas y entender cómo funcionan estos operadores.
"""

print("=" * 70)
print("OPERADORES LÓGICOS EN PYTHON - Problemas Comunes")
print("=" * 70)
print()

# Problema 1: Confusión entre 'and' y 'or'
print("Problema 1: Confusión entre 'and' y 'or'")
print("-" * 50)

edad = 25
tiene_licencia = True

# Verificación de conductor elegible
resultado1 = edad >= 18 and tiene_licencia
resultado2 = edad >= 18 or tiene_licencia
print(f"¿Es un conductor elegible (AND)? {resultado1}")
print(f"¿Es un conductor elegible (OR)? {resultado2}")
print(f"¿Son estos resultados equivalentes? {'Sí' if resultado1 == resultado2 else 'No'}")
print("¿Cuándo debería usar 'and' vs 'or'?")
print()

# Problema 2: Precedencia de operadores lógicos vs comparación
print("Problema 2: Precedencia de operadores")
print("-" * 50)

x = 5
resultado3 = x > 3 and x < 10
resultado4 = 3 < x < 10
print(f"x > 3 and x < 10: {resultado3}")
print(f"3 < x < 10: {resultado4}")
print(f"¿Son equivalentes? {'Sí' if resultado3 == resultado4 else 'No'}")
print()

# Comparaciones encadenadas sorprendentes
y = 7
resultado5 = x < y < x  # ¿Qué hace esto?
print(f"x < y < x (con x={x}, y={y}): {resultado5}")
print("¿Cómo se evalúa esto?")
print()

# Problema 3: Confusión con el operador 'not'
print("Problema 3: Confusión con 'not'")
print("-" * 50)

a = True
b = False 

print(f"not a: {not a}")
print(f"not b: {not b}")
print(f"not a and b: {not a and b}")
print(f"not (a and b): {not (a and b)}")
print("¿Por qué son diferentes?")
print()

# Problema 4: Confusión entre '==' e 'is'
print("Problema 4: '==' vs 'is'")
print("-" * 50)

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1 == lista2: {lista1 == lista2}")
print(f"lista1 is lista2: {lista1 is lista2}")
print(f"lista1 == lista3: {lista1 == lista3}")
print(f"lista1 is lista3: {lista1 is lista3}")
print("¿Qué diferencia hay entre '==' e 'is'?")
print()

# Caso especial: Números pequeños y cadenas
a = 256
b = 256
c = 257
d = 257

print(f"a = {a}, b = {b}, c = {c}, d = {d}")
print(f"a is b: {a is b}")  # True para números pequeños (implementación específica)
print(f"c is d: {c is d}")  # Puede ser False para números más grandes
print("¿Por qué 'is' funciona diferente con diferentes números?")
print()

# Problema 5: Evaluación de cortocircuito
print("Problema 5: Evaluación de cortocircuito")
print("-" * 50)

def funcion_a():
    print("Función A ejecutada")
    return True

def funcion_b():
    print("Función B ejecutada")
    return False

print("Evaluando: funcion_a() and funcion_b()")
resultado6 = funcion_a() and funcion_b()
print(f"Resultado: {resultado6}")
print()

print("Evaluando: funcion_b() and funcion_a()")
resultado7 = funcion_b() and funcion_a()
print(f"Resultado: {resultado7}")
print()

print("¿Por qué no siempre se ejecutan ambas funciones?")
print()

# Problema 6: Confusión con operadores de pertenencia
print("Problema 6: Operadores 'in' y 'not in'")
print("-" * 50)

frutas = ["manzana", "naranja", "plátano"]
print(f"Lista de frutas: {frutas}")
print(f"'manzana' in frutas: {'manzana' in frutas}")
print(f"'pera' in frutas: {'pera' in frutas}")
print(f"'pera' not in frutas: {'pera' not in frutas}")

# Con cadenas
palabra = "Python"
print(f"\nPalabra: {palabra}")
print(f"'P' in palabra: {'P' in palabra}")
print(f"'p' in palabra: {'p' in palabra}")
print(f"'th' in palabra: {'th' in palabra}")
print("¿Es 'in' sensible a mayúsculas/minúsculas?")
print()

# Problema 7: Valores que evalúan a False
print("Problema 7: Valores falsy")
print("-" * 50)

valores = [0, 0.0, "", [], {}, None, False]
print("Evaluación de valores como booleanos:")
for val in valores:
    print(f"{val} evalúa a: {bool(val)}")
print()

# Problema con valores que parecen "verdaderos"
print("Valores engañosos:")
valores_engañosos = [[''], {None: None}, " "]
for val in valores_engañosos:
    print(f"{val} evalúa a: {bool(val)}")

print("\n¿Por qué algunos valores vacíos evalúan a False y otros a True?")
print()

# Problema 8: Expresiones complejas sin parentesis
print("Problema 8: Expresiones complejas")
print("-" * 50)

p, q, r = True, False, True
resultado8 = p and q or r
resultado9 = p and (q or r)
resultado10 = (p and q) or r

print(f"p = {p}, q = {q}, r = {r}")
print(f"p and q or r = {resultado8}")
print(f"p and (q or r) = {resultado9}")
print(f"(p and q) or r = {resultado10}")
print("¿Cómo afectan los paréntesis a estas expresiones?")
print()

# Problema 9: Confusión en validación de datos
print("Problema 9: Validación de datos")
print("-" * 50)

# Validación de un nombre de usuario (debe tener entre 3 y 15 caracteres)
username = "user123"
# Formas diferentes de validar
es_valido1 = len(username) >= 3 and len(username) <= 15
es_valido2 = 3 <= len(username) <= 15

print(f"Username: '{username}'")
print(f"Validación 1 (and): {es_valido1}")
print(f"Validación 2 (comparación encadenada): {es_valido2}")
print()

# Con un nombre de usuario inválido
username_corto = "us"
es_valido1 = len(username_corto) >= 3 and len(username_corto) <= 15
es_valido2 = 3 <= len(username_corto) <= 15

print(f"Username corto: '{username_corto}'")
print(f"Validación 1 (and): {es_valido1}")
print(f"Validación 2 (comparación encadenada): {es_valido2}")
print("¿Cuál forma es más clara? ¿Son equivalentes?")
print()

# Problema 10: Lógica compleja de autorización
print("Problema 10: Autorización compleja")
print("-" * 50)

# Usuario con ciertos atributos
usuario = {
    "autenticado": True,
    "admin": False,
    "edad": 17,
    "suscripcion": "premium"
}

# ¿Puede acceder a contenido para adultos?
puede_acceder1 = usuario["autenticado"] and usuario["edad"] >= 18
# ¿Puede acceder a área administrativa?
puede_acceder2 = usuario["autenticado"] and usuario["admin"]
# ¿Puede acceder a contenido premium?
puede_acceder3 = usuario["autenticado"] and (usuario["suscripcion"] == "premium" or usuario["admin"])

print(f"Usuario: {usuario}")
print(f"¿Puede acceder a contenido para adultos? {puede_acceder1}")
print(f"¿Puede acceder a área administrativa? {puede_acceder2}")
print(f"¿Puede acceder a contenido premium? {puede_acceder3}")
print()

# Cambiando atributos
usuario["admin"] = True
print(f"Usuario con admin=True: {usuario}")
print(f"¿Ahora puede acceder a área administrativa? {usuario['autenticado'] and usuario['admin']}")
print()

print("=" * 70)
print("¿Puedes identificar todos los problemas y conceptos clave?")
print("¿Entiendes cómo se evalúan estas expresiones lógicas?")
print("=" * 70)
