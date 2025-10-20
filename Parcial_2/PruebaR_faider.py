#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRUEBAS DEL SISTEMA DE RESTAURANTE
Autor: Faider Asprilla Torres
Fecha: 20/10/2025
"""

from SistemaR_faider import *


# ===========================================================================
# BLOQUE DE PRUEBAS UNITARIAS
# ===========================================================================

def test_agregar_platos():
    print("\n" + "=" * 60)
    print("TEST: Registro de platos en el menú")
    print("=" * 60)

    sistema = SistemaRestaurante()

    # Agregar platos básicos
    sistema.agregar_plato("P001", "Filete de Res", "Plato Fuerte", 35000)
    sistema.agregar_plato("B001", "Limonada", "Bebida", 9000)
    print("✓ Platos registrados correctamente.")

    # Intentar agregar duplicado
    try:
        sistema.agregar_plato("P001", "Repetido", "Plato Fuerte", 10000)
    except KeyError:
        print("✓ Duplicado detectado correctamente.")

    print("✓ Prueba completada.")


def test_reservar_mesa():
    print("\n" + "=" * 60)
    print("TEST: Reservar mesas del restaurante")
    print("=" * 60)

    sistema = SistemaRestaurante()

    # Configurar mesa inicial
    sistema.configurar_mesa(1, 4)

    # Reserva válida
    sistema.reservar_mesa(1, 3, "12:00")
    print("✓ Reserva creada con éxito.")

    # Mesa ocupada
    try:
        sistema.reservar_mesa(1, 2, "13:00")
    except MesaNoDisponible:
        print("✓ Error por mesa ocupada controlado.")

    # Capacidad excedida
    sistema.configurar_mesa(2, 5)
    try:
        sistema.reservar_mesa(2, 10, "14:00")
    except CapacidadExcedida:
        print("✓ Capacidad excedida detectada correctamente.")

    print("✓ Prueba completada.")


def test_crear_pedido():
    print("\n" + "=" * 60)
    print("TEST: Creación de pedidos")
    print("=" * 60)

    sistema = SistemaRestaurante()
    sistema.configurar_mesa(1, 4)
    sistema.reservar_mesa(1, 2, "13:00")

    id_pedido = sistema.crear_pedido(1)
    print(f"✓ Pedido generado con ID {id_pedido}")

    try:
        sistema.crear_pedido(2)
    except PedidoInvalido:
        print("✓ Control de pedido inválido correcto.")

    print("✓ Prueba completada.")


def test_agregar_items():
    print("\n" + "=" * 60)
    print("TEST: Agregar ítems al pedido")
    print("=" * 60)

    sistema = SistemaRestaurante()
    sistema.agregar_plato("P001", "Filete", "Plato fuerte", 35000)
    sistema.agregar_plato("B001", "Limonada", "Bebida", 9000)

    sistema.configurar_mesa(1, 4)
    sistema.reservar_mesa(1, 2, "14:00")
    pid = sistema.crear_pedido(1)

    sistema.agregar_item(pid, "P001", 2)
    sistema.agregar_item(pid, "B001", 1)
    print("✓ Ítems agregados con éxito.")

    try:
        sistema.agregar_item(pid, "X999", 1)
    except PlatoNoEncontrado:
        print("✓ Plato inexistente correctamente manejado.")

    print("✓ Prueba completada.")


def test_calcular_y_pagar():
    print("\n" + "=" * 60)
    print("TEST: Calcular y procesar pago")
    print("=" * 60)

    sistema = SistemaRestaurante()
    sistema.agregar_plato("P001", "Filete de Res", "Plato Fuerte", 35000)
    sistema.agregar_plato("B001", "Limonada", "Bebida", 9000)

    sistema.configurar_mesa(1, 4)
    sistema.reservar_mesa(1, 2, "15:00")
    pedido = sistema.crear_pedido(1)

    sistema.agregar_item(pedido, "P001", 2)
    sistema.agregar_item(pedido, "B001", 3)

    totales = sistema.calcular_total(pedido, propina_porcentaje=0.18)
    print(f"✓ Total calculado: ${totales['total']:.2f}")

    pago = sistema.pagar_pedido(pedido)
    print(f"✓ Pago registrado: {pago}")

    print("✓ Prueba completada.")


def test_reportes():
    print("\n" + "=" * 60)
    print("TEST: Reportes y estadísticas")
    print("=" * 60)

    sistema = SistemaRestaurante()
    sistema.agregar_plato("P001", "Filete", "Plato Fuerte", 35000)
    sistema.agregar_plato("B001", "Limonada", "Bebida", 9000)

    sistema.configurar_mesa(1, 4)
    sistema.reservar_mesa(1, 2, "16:00")

    pid = sistema.crear_pedido(1)
    sistema.agregar_item(pid, "P001", 2)
    sistema.agregar_item(pid, "B001", 1)
    sistema.pagar_pedido(pid)

    print("✓ Platos más vendidos:", sistema.platos_mas_vendidos())
    print("✓ Ventas por categoría:", sistema.ventas_por_categoria())
    print("✓ Ventas del día:", sistema.reporte_ventas_dia())
    print("✓ Estado del restaurante:", sistema.estado_restaurante())

    print("✓ Prueba completada.")


def test_exportar_importar():
    print("\n" + "=" * 60)
    print("TEST: Exportar e importar menú")
    print("=" * 60)

    sistema = SistemaRestaurante()
    sistema.agregar_plato("P001", "Filete de Res", "Plato Fuerte", 35000)
    sistema.agregar_plato("B001", "Limonada", "Bebida", 9000)

    sistema.exportar_menu("menu_test.txt")
    print("✓ Menú exportado exitosamente.")

    nuevo = SistemaRestaurante()
    resultado = nuevo.importar_menu("menu_test.txt")
    print(f"✓ Platos importados: {resultado['platos_importados']}")

    print("✓ Prueba completada.")


def test_excepciones():
    print("\n" + "=" * 60)
    print("TEST: Validación de excepciones")
    print("=" * 60)

    sistema = SistemaRestaurante()
    try:
        sistema.crear_pedido(1)
    except PedidoInvalido as e:
        print(f"✓ Pedido inválido correctamente detectado: {e}")

    try:
        raise PlatoNoEncontrado("Z999")
    except PlatoNoEncontrado as e:
        print(f"✓ Excepción personalizada detectada: {e}")

    print("✓ Prueba completada.")


# ===========================================================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ===========================================================================
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" EJECUCIÓN DE TODAS LAS PRUEBAS DEL SISTEMA DE RESTAURANTE ")
    print("=" * 70)

    pruebas = [
        test_agregar_platos,
        test_reservar_mesa,
        test_crear_pedido,
        test_agregar_items,
        test_calcular_y_pagar,
        test_reportes,
        test_exportar_importar,
        test_excepciones
    ]

    total = len(pruebas)
    correctas = 0

    for test in pruebas:
        try:
            test()
            correctas += 1
        except Exception as e:
            print(f"✗ Error en {test.__name__}: {e}")

    print("\n" + "=" * 70)
    print("RESULTADO FINAL DE PRUEBAS")
    print("=" * 70)
    print(f"✓ Pruebas superadas: {correctas}/{total}")
    print("=" * 70)
