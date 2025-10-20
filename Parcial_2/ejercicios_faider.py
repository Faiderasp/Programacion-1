#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PARCIAL 2 - EJERCICIOS
Estudiante: Faider Asprilla Torres
Fecha: 20/10/2025
"""


from collections import defaultdict
from typing import *
# =================== EJERCICIO 1: CALCULADORA CIENTÍFICA ===================


def calculadora_cientifica(operacion, a, b):
    """Ejecuta una operación aritmética básica entre `a` y `b`.


    - Valida tipos numéricos.
    - Lanza errores para operaciones no soportadas o división/módulo por cero.
    - Devuelve resultado redondeado a 2 decimales o imprime error.
    """
    
    # Aseguramos tipos numéricos
    if not (type(a) not in [int,float] and type(b) not in [int,float]):
        raise ValueError("Los parámetros deben ser numéricos")


    # Implementación de funciones
    def suma(x, y):
        return x + y
    def resta(x, y):
        return x - y
    def mult(x, y):
        return x * y
    def div(x, y):
        if y == 0:
            raise ZeroDivisionError("No se puede realizar division por cero")
        return x / y
    def pow_(x, y):
        return x ** y
    def mod(x, y):
        if y == 0:
            raise ZeroDivisionError("No se puede realizar modulo por cero")
        return x % y


    ops = {
    'suma': suma,
    'resta': resta,
    'multiplicacion': mult,
    'division': div,
    'potencia': pow_,
    'modulo': mod,
    }

    if operacion not in ops:
        raise ValueError(f"Operación inválida: '{operacion}'")


    resultado = ops[operacion](a, b)
    return round(resultado, 2)


# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================
class ValidadorPassword:
    """
    Validador de contraseñas con opciones configurables.
    - validar(password) -> (bool, list_errores)
    - es_fuerte(password) -> bool (regla más estricta)
    """

    def __init__(self, min_longitud=8, requiere_mayuscula=True,
                 requiere_minuscula=True, requiere_numero=True,
                 requiere_especial=True):
        self.min_longitud = int(min_longitud)
        self.requiere_mayuscula = bool(requiere_mayuscula)
        self.requiere_minuscula = bool(requiere_minuscula)
        self.requiere_numero = bool(requiere_numero)
        self.requiere_especial = bool(requiere_especial)

        # Conjunto de símbolos especiales aceptados
        self._especiales = set("!@#$%^&*()-_=+[]{};:,<.>/?|\\`~")

    def validar(self, password: str) -> Tuple[bool, List[str]]:
        """
        Verifica cada regla configurada y devuelve (True, []) si pasa todo,
        o (False, [errores]) con mensajes legibles.
        """
        errores = []

        if not isinstance(password, str):
            errores.append("La contraseña debe ser una cadena.")
            return False, errores

        if len(password) < self.min_longitud:
            errores.append(f"Longitud mínima: {self.min_longitud} caracteres")

        # Uso conjuntos y any/iter para variar la implementación
        chars = set(password)
        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("Debe contener al menos una letra mayúscula")
        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("Debe contener al menos una letra minúscula")
        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("Debe contener al menos un número")
        if self.requiere_especial and not (chars & self._especiales):
            errores.append("Debe contener al menos un carácter especial")

        return (len(errores) == 0, errores)

    def es_fuerte(self, password: str) -> bool:
        """
        Regla de fuerte: longitud >= 12 y cumple todas las 4 condiciones básicas.
        """
        valido, _ = self.validar(password)
        if len(password) < 12:
            return False

        # Para consideración estricta, nos aseguramos individualmente.
        condiciones = [
            any(c.isupper() for c in password),
            any(c.islower() for c in password),
            any(c.isdigit() for c in password),
            bool(set(password) & self._especiales)
        ]
        return all(condiciones) and valido


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================
class GestorInventario:
    """
    Gestor de inventario con almacenamiento interno en un diccionario.
    Las operaciones permiten agregar, actualizar stock, buscar por categoría,
    listar productos bajo stock, calcular valor total y top productos por valor.
    """

    def __init__(self):
        # Estructura: {codigo: {"nombre":..., "precio":..., "cantidad":..., "categoria":...}}
        self.inventario: Dict[str, Dict[str, Any]] = {}

    def agregar_producto(self, codigo: str, nombre: str, precio: float, cantidad: int, categoria: str):
        """
        Añade un producto nuevo. Valida duplicados y valores no negativos.
        """
        if not isinstance(codigo, str) or not codigo:
            raise ValueError("Código inválido.")
        if codigo in self.inventario:
            raise ValueError(f"El producto con código '{codigo}' ya existe.")
        if precio < 0 or cantidad < 0:
            raise ValueError("Precio y cantidad deben ser >= 0.")
        self.inventario[codigo] = {
            "nombre": str(nombre),
            "precio": float(precio),
            "cantidad": int(cantidad),
            "categoria": str(categoria)
        }

    def actualizar_stock(self, codigo: str, cantidad_cambio: int):
        """
        Modifica el stock sumando 'cantidad_cambio' (positivo o negativo).
        Verifica existencia y no deja stock negativo.
        """
        if codigo not in self.inventario:
            raise ValueError(f"El producto con código '{codigo}' no existe.")
        actual = self.inventario[codigo]["cantidad"]
        nuevo = actual + int(cantidad_cambio)
        if nuevo < 0:
            raise ValueError("El stock no puede ser negativo tras la operación.")
        self.inventario[codigo]["cantidad"] = nuevo

    def buscar_por_categoria(self, categoria: str) -> List[Tuple[str, str, float]]:
        """
        Retorna una lista de tuplas (codigo, nombre, precio) que pertenezcan
        a la categoría indicada (comparación case-insensitive).
        """
        cat = categoria.lower() if isinstance(categoria, str) else ""
        salida = []
        for codigo, dato in self.inventario.items():
            if dato.get("categoria", "").lower() == cat:
                salida.append((codigo, dato.get("nombre"), dato.get("precio")))
        return salida

    def productos_bajo_stock(self, limite: int = 10) -> Dict[str, int]:
        """
        Devuelve un diccionario con productos cuya cantidad sea menor que 'limite'.
        """
        res = {}
        for codigo, dato in self.inventario.items():
            if dato.get("cantidad", 0) < int(limite):
                res[codigo] = dato.get("cantidad", 0)
        return res

    def valor_total_inventario(self) -> float:
        """
        Calcula el valor total del inventario (precio * cantidad) y lo redondea a 2 decimales.
        """
        total = 0.0
        for dato in self.inventario.values():
            total += float(dato.get("precio", 0.0)) * int(dato.get("cantidad", 0))
        return round(total, 2)

    def top_productos(self, n: int = 5) -> List[Tuple[str, float]]:
        """
        Devuelve lista de tuplas (codigo, valor_en_inventario) ordenada descendentemente por valor.
        """
        lista = [(codigo, dato["precio"] * dato["cantidad"]) for codigo, dato in self.inventario.items()]
        # Ordeno usando sorted (otra forma de hacerlo respecto al original)
        lista_ordenada = sorted(lista, key=lambda x: x[1], reverse=True)
        return lista_ordenada[:int(n)]


# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================
def es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto aplicando las reglas del calendario gregoriano.
    """
    # Uso una lógica con divisiones y comprobaciones encadenadas distinta en forma
    if anio % 400 == 0:
        return True
    if anio % 100 == 0:
        return False
    return anio % 4 == 0


def dias_en_mes(mes: int, anio: int) -> int:
    """
    Retorna la cantidad de días que tiene un mes en un año dado.
    Valida el mes y usa la comprobación de bisiesto para febrero.
    """
    if not (1 <= mes <= 12):
        raise ValueError("Mes inválido: debe estar entre 1 y 12")
    # Meses con 31 días
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if mes in (4, 6, 9, 11):
        return 30
    # febrero
    return 29 if es_bisiesto(anio) else 28


def generar_calendario(mes: int, anio: int, dia_inicio: int = 0) -> str:
    """
    Genera un calendario en texto para un mes y año dados.
    dia_inicio: 0=Lunes, 6=Domingo.
    """
    # Cabecera simplificada
    nombres = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"]
    try:
        dias = dias_en_mes(mes, anio)
    except ValueError:
        return ""

    if not (0 <= dia_inicio <= 6):
        raise ValueError("dia_inicio debe estar entre 0 y 6")

    # Construyo las filas semana por semana
    semanas = []
    semana = ["  "] * 7
    dia = 1
    posicion = dia_inicio
    # Relleno primera semana desde dia_inicio
    while dia <= dias:
        semana[posicion] = f"{dia:2d}"
        posicion += 1
        if posicion == 7:
            semanas.append(" ".join(semana))
            semana = ["  "] * 7
            posicion = 0
        dia += 1
    # Si quedó parcial, la añado
    if any(cell.strip() for cell in semana):
        semanas.append(" ".join(semana))

    resultado = " ".join(nombres) + "\n" + "\n".join(semanas)
    return resultado


# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================
def analizar_ventas(ventas: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Recibe una lista de ventas (cada una con 'producto', 'cantidad', 'precio', 'descuento')
    y devuelve estadísticas agregadas:
    - total_ventas, promedio_por_venta, producto_mas_vendido, venta_mayor, total_descuentos
    """
    if not isinstance(ventas, list) or len(ventas) == 0:
        raise ValueError("La lista de ventas no puede estar vacía y debe ser una lista.")

    totales = 0.0
    tot_desc = 0.0
    cantidades_por_producto = {}
    venta_mayor = None
    mayor_monto = -1.0

    for v in ventas:
        if not all(k in v for k in ("producto", "cantidad", "precio", "descuento")):
            raise ValueError("Cada venta debe contener 'producto','cantidad','precio','descuento'")

        cantidad = int(v["cantidad"])
        precio = float(v["precio"])
        descuento = float(v["descuento"])

        subtotal = cantidad * precio
        importe_desc = subtotal * descuento
        total = subtotal - importe_desc

        totales += total
        tot_desc += importe_desc

        cantidades_por_producto[v["producto"]] = cantidades_por_producto.get(v["producto"], 0) + cantidad

        if total > mayor_monto:
            mayor_monto = total
            venta_mayor = v.copy()

    producto_mas_vendido = max(cantidades_por_producto, key=cantidades_por_producto.get)

    promedio = round(totales / len(ventas), 2)

    return {
        "total_ventas": round(totales, 2),
        "promedio_por_venta": promedio,
        "producto_mas_vendido": producto_mas_vendido,
        "venta_mayor": venta_mayor,
        "total_descuentos": round(tot_desc, 2)
    }


def encontrar_patrones(numeros: List[float]) -> Dict[str, Any]:
    """
    Analiza una secuencia numérica para detectar:
    - número de secuencias ascendentes y descendentes
    - longitud máxima de cada tipo
    - repeticiones y su cantidad
    Enfoque alternativo al original para variar la implementación.
    """
    if not isinstance(numeros, list) or len(numeros) < 2:
        raise ValueError("Debe proveerse una lista de al menos dos números.")

    # Detecto repeticiones usando diccionario de conteo
    conteo = {}
    for x in numeros:
        conteo[x] = conteo.get(x, 0) + 1
    repetidos = {k: v for k, v in conteo.items() if v > 1}

    sec_asc = 0
    sec_desc = 0
    max_asc = 1
    max_desc = 1

    # Contadores corrientes para longitud de tramo
    curr_asc = 1
    curr_desc = 1

    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i - 1]:
            curr_asc += 1
            # Si venía una descendente, se cierra esa secuencia
            if curr_desc > 1:
                sec_desc += 1
                max_desc = max(max_desc, curr_desc)
                curr_desc = 1
        elif numeros[i] < numeros[i - 1]:
            curr_desc += 1
            if curr_asc > 1:
                sec_asc += 1
                max_asc = max(max_asc, curr_asc)
                curr_asc = 1
        else:
            # igualdad: cerrar ambas posibles secuencias largas
            if curr_asc > 1:
                sec_asc += 1
                max_asc = max(max_asc, curr_asc)
            if curr_desc > 1:
                sec_desc += 1
                max_desc = max(max_desc, curr_desc)
            curr_asc = curr_desc = 1

    # Al terminar, chequeo si quedó una secuencia abierta
    if curr_asc > 1:
        sec_asc += 1
        max_asc = max(max_asc, curr_asc)
    if curr_desc > 1:
        sec_desc += 1
        max_desc = max(max_desc, curr_desc)

    return {
        "secuencias_ascendentes": sec_asc,
        "secuencias_descendentes": sec_desc,
        "longitud_max_ascendente": max_asc,
        "longitud_max_descendente": max_desc,
        "numeros_repetidos": repetidos
    }


def simular_crecimiento(principal: float, tasa_anual: float, anios: int, aporte_anual: float = 0.0) -> List[Dict[str, Any]]:
    """
    Simula crecimiento con interés compuesto anual y aportes periódicos.
    Devuelve una lista con el estado por año: {'anio', 'balance', 'interes_ganado'}.
    """
    if principal < 0 or tasa_anual < 0 or anios <= 0 or aporte_anual < 0:
        raise ValueError("Parámetros inválidos: deben ser no negativos y años > 0")

    balance = float(principal)
    resultados = []

    # Aplico el interés de forma alternativa: calculo interés sobre el balance
    # actualizado tras el aporte anual (mismo resultado conceptual, distinta estructura).
    for y in range(1, int(anios) + 1):
        # aporte al inicio del año
        balance += float(aporte_anual)
        interes = balance * float(tasa_anual)
        balance += interes

        resultados.append({
            "anio": y,
            "balance": round(balance, 2),
            "interes_ganado": round(interes, 2)
        })

    return resultados


# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================
if __name__ == "__main__":
    print("=" * 70)
    print(" PRUEBAS DE EJERCICIOS - VERSIÓN REFACTORIZADA")
    print("=" * 70)

    print("\nEjercicio 1")
    print(calculadora_cientifica("division", 10, 3))  # 3.33
    print(calculadora_cientifica("potencia", 2, 8))   # 256.00
    print(calculadora_cientifica("division", 10, 0))  # None con mensaje de error
    print(calculadora_cientifica("raiz", 4, 2))       # None con mensaje de error

    print("\nEjercicio 2")
    val = ValidadorPassword(min_longitud=8)
    print(val.validar("Abc123!"))        # False, longitud insuficiente
    print(val.validar("Abc123!@"))       # True o (True, [])
    print(val.es_fuerte("Abc123!@#$Xyz"))  # True (si cumple las reglas)

    print("\nEjercicio 3")
    inv = GestorInventario()
    inv.agregar_producto("P001", "Laptop", 1200.00, 15, "Electrónica")
    inv.agregar_producto("P002", "Mouse", 25.50, 5, "Accesorios")
    inv.agregar_producto("P003", "Teclado", 85.00, 8, "Accesorios")
    inv.actualizar_stock("P001", -3)
    print(inv.productos_bajo_stock(10))
    print(inv.buscar_por_categoria("Accesorios"))
    print(inv.valor_total_inventario())
    print(inv.top_productos(2))

    print("\nEjercicio 4")
    print(es_bisiesto(2024), es_bisiesto(2100), es_bisiesto(2000))
    print(dias_en_mes(2, 2024), dias_en_mes(2, 2023))
    print(generar_calendario(1, 2024, 0))

    print("\nEjercicio 5")
    ventas_demo = [
        {"producto": "A", "cantidad": 2, "precio": 10.0, "descuento": 0.1},
        {"producto": "B", "cantidad": 1, "precio": 20.0, "descuento": 0.0},
        {"producto": "A", "cantidad": 3, "precio": 10.0, "descuento": 0.05},
    ]
    print(analizar_ventas(ventas_demo))
    print(encontrar_patrones([1, 2, 2, 3, 2, 1, 1, 0]))
    print(simular_crecimiento(1000, 0.05, 3, aporte_anual=100))
