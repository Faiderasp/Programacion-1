#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PARCIAL 2 - SISTEMA RESTAURANTE
Estudiante: Faider Asprilla Torres
Fecha: 20/10/2025
"""

from datetime import datetime
import json


# ===========================================================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================================================
class ErrorRestaurante(Exception):
    """Clase base para errores del sistema."""
    pass


class PlatoNoEncontrado(ErrorRestaurante):
    def __init__(self, codigo):
        super().__init__(f"El plato con código '{codigo}' no se encuentra en el menú.")


class MesaNoDisponible(ErrorRestaurante):
    def __init__(self, numero):
        super().__init__(f"La mesa número {numero} ya está ocupada o reservada.")


class CapacidadExcedida(ErrorRestaurante):
    def __init__(self, numero, capacidad, personas):
        super().__init__(f"La mesa {numero} tiene capacidad para {capacidad}, no para {personas} personas.")


class PedidoInvalido(ErrorRestaurante):
    def __init__(self, motivo):
        super().__init__(f"Pedido inválido: {motivo}")


# ===========================================================================
# CLASE PRINCIPAL
# ===========================================================================
class SistemaRestaurante:
    """
    Sistema para gestionar platos, mesas, pedidos y ventas.
    Incluye funciones de reporte, exportación y control de disponibilidad.
    """

    def __init__(self):
        self.menu = {}
        self.mesas = {}
        self.pedidos = {}
        self.ventas = []
        self._contador_pedidos = 0

    # ===================== PLATOS =====================

    def agregar_plato(self, codigo, nombre, categoria, precio):
        """Agrega un nuevo plato al menú del restaurante."""
        if codigo in self.menu:
            raise KeyError(f"Ya existe un plato con código {codigo}")
        if not nombre.strip() or precio <= 0:
            raise ValueError("El nombre no puede estar vacío y el precio debe ser positivo.")

        self.menu[codigo] = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "ventas": 0
        }

    def eliminar_plato(self, codigo):
        """Elimina un plato del menú, si existe."""
        if codigo not in self.menu:
            raise PlatoNoEncontrado(codigo)
        del self.menu[codigo]

    def actualizar_precio(self, codigo, nuevo_precio):
        """Actualiza el precio de un plato existente."""
        if codigo not in self.menu:
            raise PlatoNoEncontrado(codigo)
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser positivo.")
        self.menu[codigo]["precio"] = float(nuevo_precio)

    def exportar_menu(self, ruta="menu.txt"):
        """Guarda el menú actual en un archivo plano."""
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                for codigo, plato in self.menu.items():
                    f.write(f"{codigo}|{plato['nombre']}|{plato['categoria']}|{plato['precio']}\n")
        except Exception as e:
            print(f"Error al exportar menú: {e}")

    def importar_menu(self, ruta="menu.txt"):
        """Carga los platos desde un archivo, validando línea por línea."""
        cargados = 0
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        codigo, nombre, categoria, precio = linea.strip().split("|")
                        if codigo not in self.menu:
                            self.agregar_plato(codigo, nombre, categoria, float(precio))
                            cargados += 1
                    except Exception:
                        continue
        except FileNotFoundError:
            print(f"No se encontró el archivo '{ruta}'")
        return {"platos_importados": cargados}

    # ===================== MESAS =====================

    def configurar_mesa(self, numero, capacidad):
        """Agrega o configura una mesa con su capacidad."""
        if numero <= 0 or capacidad < 1:
            raise ValueError("Número o capacidad de mesa inválidos.")
        self.mesas[numero] = {
            "capacidad": int(capacidad),
            "reservada": False,
            "personas": 0,
            "hora": None
        }

    def reservar_mesa(self, numero, personas, hora):
        """Marca una mesa como reservada, si hay espacio suficiente."""
        if numero not in self.mesas:
            raise KeyError(f"La mesa {numero} no existe.")
        mesa = self.mesas[numero]

        if mesa["reservada"]:
            raise MesaNoDisponible(numero)
        if personas > mesa["capacidad"]:
            raise CapacidadExcedida(numero, mesa["capacidad"], personas)

        mesa["reservada"] = True
        mesa["personas"] = int(personas)
        mesa["hora"] = hora

    def liberar_mesa(self, numero):
        """Libera una mesa para ser usada nuevamente."""
        if numero not in self.mesas:
            raise KeyError("La mesa indicada no existe.")
        mesa = self.mesas[numero]
        mesa.update({"reservada": False, "personas": 0, "hora": None})

    # ===================== PEDIDOS =====================

    def crear_pedido(self, numero_mesa):
        """Crea un nuevo pedido para una mesa ya reservada."""
        if numero_mesa not in self.mesas:
            raise PedidoInvalido("La mesa indicada no existe.")
        mesa = self.mesas[numero_mesa]
        if not mesa["reservada"]:
            raise PedidoInvalido("La mesa no está reservada.")
        self._contador_pedidos += 1
        codigo = f"PED-{self._contador_pedidos:04d}"
        self.pedidos[codigo] = {
            "mesa": numero_mesa,
            "items": [],
            "total": 0.0,
            "pagado": False,
            "fecha": datetime.now()
        }
        return codigo

    def agregar_item(self, id_pedido, codigo_plato, cantidad):
        """Agrega ítems al pedido seleccionado."""
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("No existe ese pedido.")
        if codigo_plato not in self.menu:
            raise PlatoNoEncontrado(codigo_plato)
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        pedido = self.pedidos[id_pedido]
        plato = self.menu[codigo_plato]

        subtotal = plato["precio"] * cantidad
        pedido["items"].append({
            "codigo": codigo_plato,
            "nombre": plato["nombre"],
            "cantidad": cantidad,
            "subtotal": subtotal
        })

        pedido["total"] += subtotal
        self.menu[codigo_plato]["ventas"] += cantidad

    def calcular_total(self, id_pedido, propina_porcentaje=0.1, impuestos=0.08):
        """Calcula el total de un pedido aplicando impuestos y propina."""
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido inexistente.")
        pedido = self.pedidos[id_pedido]

        subtotal = pedido["total"]
        propina = subtotal * float(propina_porcentaje)
        iva = subtotal * float(impuestos)
        total = subtotal + propina + iva

        return {
            "subtotal": round(subtotal, 2),
            "iva": round(iva, 2),
            "propina": round(propina, 2),
            "total": round(total, 2)
        }

    def pagar_pedido(self, id_pedido):
        """Procesa el pago del pedido, marca mesa como libre y almacena venta."""
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("No existe ese pedido.")
        pedido = self.pedidos[id_pedido]
        if pedido["pagado"]:
            raise PedidoInvalido("El pedido ya fue pagado.")

        totales = self.calcular_total(id_pedido)
        pedido["pagado"] = True

        mesa = self.mesas[pedido["mesa"]]
        mesa["reservada"] = False
        mesa["personas"] = 0
        mesa["hora"] = None

        self.ventas.append({
            "id_pedido": id_pedido,
            "total": totales["total"],
            "fecha": datetime.now()
        })

        return {"id_pedido": id_pedido, "total_pagado": totales["total"], "fecha": datetime.now().isoformat()}

    # ===================== REPORTES =====================

    def platos_mas_vendidos(self, n=5):
        """Retorna los platos con mayor cantidad de ventas."""
        ranking = sorted(
            [(c, d["nombre"], d["ventas"]) for c, d in self.menu.items()],
            key=lambda x: x[2],
            reverse=True
        )
        return ranking[:n]

    def ventas_por_categoria(self):
        """Agrupa las ventas por categoría de plato."""
        categorias = {}
        for pedido in self.pedidos.values():
            for item in pedido["items"]:
                codigo = item["codigo"]
                categoria = self.menu[codigo]["categoria"]
                categorias[categoria] = categorias.get(categoria, 0) + item["subtotal"]
        return {c: round(v, 2) for c, v in categorias.items()}

    def reporte_ventas_dia(self, fecha=None):
        """Devuelve un resumen de ventas filtrado por fecha (por defecto hoy)."""
        if fecha is None:
            fecha = datetime.now().date()
        total_dia = sum(v["total"] for v in self.ventas if v["fecha"].date() == fecha)
        cantidad = len([v for v in self.ventas if v["fecha"].date() == fecha])
        promedio = total_dia / cantidad if cantidad > 0 else 0
        return {
            "fecha": str(fecha),
            "ventas_totales": round(total_dia, 2),
            "cantidad_pedidos": cantidad,
            "promedio_por_pedido": round(promedio, 2)
        }

    def estado_restaurante(self):
        """Devuelve un resumen general del restaurante."""
        mesas_total = len(self.mesas)
        ocupadas = sum(1 for m in self.mesas.values() if m["reservada"])
        disponibles = mesas_total - ocupadas
        return {
            "mesas_total": mesas_total,
            "mesas_ocupadas": ocupadas,
            "mesas_disponibles": disponibles,
            "platos_menu": len(self.menu),
            "pedidos_abiertos": sum(1 for p in self.pedidos.values() if not p["pagado"])
        }

    # ===================== ARCHIVOS Y DATOS =====================

    def exportar_datos(self, archivo="restaurante_data.json"):
        """Guarda todo el sistema en un archivo JSON."""
        try:
            data = {
                "menu": self.menu,
                "mesas": self.mesas,
                "pedidos": self.pedidos,
                "ventas": self.ventas
            }
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def importar_datos(self, archivo="restaurante_data.json"):
        """Carga la información completa desde un archivo JSON."""
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.menu = data.get("menu", {})
            self.mesas = data.get("mesas", {})
            self.pedidos = data.get("pedidos", {})
            self.ventas = data.get("ventas", [])
        except FileNotFoundError:
            print(f"Archivo '{archivo}' no encontrado.")
        except Exception as e:
            print(f"Error al importar datos: {e}")


# ===========================================================================
# PRUEBA MANUAL
# ===========================================================================
if __name__ == "__main__":
    print("=" * 70)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE ")
    print("=" * 70)

    r = SistemaRestaurante()
    r.agregar_plato("P001", "Filete de Res", "Plato Fuerte", 35000)
    r.agregar_plato("B001", "Limonada", "Bebida", 9000)
    r.configurar_mesa(1, 4)
    r.reservar_mesa(1, 2, "13:00")
    pedido = r.crear_pedido(1)
    r.agregar_item(pedido, "P001", 2)
    r.agregar_item(pedido, "B001", 1)
    print("Totales:", r.calcular_total(pedido, 0.1))
    print("Pago:", r.pagar_pedido(pedido))
    print("Reporte diario:", r.reporte_ventas_dia())
    print("Estado actual:", r.estado_restaurante())
