#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRUEBAS DEL SISTEMA DE BIBLIOTECA
Autor: Faider Asprilla Torres
Fecha: 20/10/2025
"""

from sistemaB_faider import *


# ===========================================================================
# FUNCIONES DE PRUEBA
# ===========================================================================

def prueba_agregar_y_buscar_libros():
    print("\n" + "=" * 60)
    print("TEST: Registro y búsqueda de libros")
    print("=" * 60)

    sistema = SistemaBiblioteca()

    # Registro de libros válidos
    sistema.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    sistema.agregar_libro("9781492051367", "Fluent Python", "Luciano Ramalho", 2020, "Programación", 4)
    print("✓ Libros agregados con éxito.")

    # Intento de duplicado
    try:
        sistema.agregar_libro("9780134685991", "Duplicado", "Otro", 2018, "General", 1)
    except KeyError:
        print("✓ Duplicado correctamente rechazado.")

    # Búsqueda por título parcial
    resultado = sistema.buscar_libros("titulo", "python")
    print(f"✓ Resultados encontrados: {len(resultado)}")

    print("✓ Prueba completada.")


def prueba_registro_y_estado_usuario():
    print("\n" + "=" * 60)
    print("TEST: Registro y estado del usuario")
    print("=" * 60)

    sistema = SistemaBiblioteca()
    sistema.registrar_usuario("U001", "Ana Gómez", "ana@correo.com")

    estado = sistema.obtener_estado_usuario("U001")
    print(f"✓ Usuario {estado['nombre']} puede prestar: {estado['puede_prestar']}")

    # Error por duplicado
    try:
        sistema.registrar_usuario("U001", "Otro", "otro@correo.com")
    except ValueError:
        print("✓ Duplicado de usuario controlado correctamente.")

    print("✓ Prueba completada.")


def prueba_prestamo_y_devolucion():
    print("\n" + "=" * 60)
    print("TEST: Flujo de préstamo y devolución")
    print("=" * 60)

    sistema = SistemaBiblioteca(dias_prestamo=5, multa_por_dia=2.0)

    sistema.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 2)
    sistema.registrar_usuario("U001", "Carlos Pérez", "carlos@correo.com")

    id_prestamo = sistema.prestar_libro("9780134685991", "U001")
    print(f"✓ Préstamo creado: {id_prestamo}")

    # Simular retraso
    sistema.prestamos[id_prestamo]["fecha_vencimiento"] = datetime.now() - timedelta(days=3)
    devolucion = sistema.devolver_libro(id_prestamo)
    print(f"✓ Multa generada: {devolucion['multa']}")

    print("✓ Prueba completada.")


def prueba_renovacion_y_limites():
    print("\n" + "=" * 60)
    print("TEST: Renovaciones y límites de préstamo")
    print("=" * 60)

    sistema = SistemaBiblioteca()

    sistema.agregar_libro("9781492051367", "Fluent Python", "Luciano Ramalho", 2020, "Programación", 1)
    sistema.registrar_usuario("U001", "Sofía López", "sofia@correo.com")

    pid = sistema.prestar_libro("9781492051367", "U001")
    mensaje = sistema.renovar_prestamo(pid)
    print("✓", mensaje)

    # Simular vencimiento
    sistema.prestamos[pid]["fecha_vencimiento"] = datetime.now() - timedelta(days=2)
    try:
        sistema.renovar_prestamo(pid)
    except PrestamoVencido as e:
        print(f"✓ Renovación rechazada correctamente: {e}")

    print("✓ Prueba completada.")


def prueba_reportes():
    print("\n" + "=" * 60)
    print("TEST: Reportes del sistema")
    print("=" * 60)

    sistema = SistemaBiblioteca()

    sistema.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    sistema.agregar_libro("9781492051367", "Fluent Python", "Luciano Ramalho", 2020, "Programación", 5)
    sistema.registrar_usuario("U001", "Marcos Ruiz", "marcos@correo.com")

    p1 = sistema.prestar_libro("9780134685991", "U001")
    sistema.devolver_libro(p1)
    p2 = sistema.prestar_libro("9781492051367", "U001")
    sistema.devolver_libro(p2)

    print("✓ Libros más prestados:", sistema.libros_mas_prestados(2))
    print("✓ Usuarios más activos:", sistema.usuarios_mas_activos())
    print("✓ Estadísticas por categoría:", sistema.estadisticas_categoria("Programación"))
    print("✓ Préstamos vencidos:", sistema.prestamos_vencidos())
    print("✓ Reporte financiero:", sistema.reporte_financiero())

    print("✓ Prueba completada.")


def prueba_exportar_e_importar():
    print("\n" + "=" * 60)
    print("TEST: Exportar e importar catálogo")
    print("=" * 60)

    sistema = SistemaBiblioteca()
    sistema.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    sistema.agregar_libro("9781492051367", "Fluent Python", "Luciano Ramalho", 2020, "Programación", 5)

    sistema.exportar_catalogo("catalogo_test.txt")
    print("✓ Exportación exitosa.")

    sistema2 = SistemaBiblioteca()
    resultado = sistema2.importar_catalogo("catalogo_test.txt")
    print(f"✓ Libros cargados: {resultado['exitosos']}")

    print("✓ Prueba completada.")


def prueba_excepciones_directas():
    print("\n" + "=" * 60)
    print("TEST: Excepciones personalizadas")
    print("=" * 60)

    sistema = SistemaBiblioteca()
    try:
        sistema.devolver_libro("X999")
    except KeyError:
        print("✓ Excepción controlada al devolver préstamo inexistente.")

    try:
        raise LibroNoDisponible("9999999999999", "Inexistente")
    except LibroNoDisponible as e:
        print(f"✓ Error personalizado: {e}")

    print("✓ Prueba completada.")


# ===========================================================================
# EJECUCIÓN GENERAL
# ===========================================================================
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" PRUEBAS DEL SISTEMA DE GESTIÓN DE BIBLIOTECA ")
    print("=" * 70)

    pruebas = [
        prueba_agregar_y_buscar_libros,
        prueba_registro_y_estado_usuario,
        prueba_prestamo_y_devolucion,
        prueba_renovacion_y_limites,
        prueba_reportes,
        prueba_exportar_e_importar,
        prueba_excepciones_directas
    ]

    total = len(pruebas)
    exitosas = 0

    for test in pruebas:
        try:
            test()
            exitosas += 1
        except Exception as e:
            print(f"✗ Fallo en {test.__name__}: {e}")

    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    print(f"✓ Pruebas exitosas: {exitosas}/{total}")
    print("=" * 70)
