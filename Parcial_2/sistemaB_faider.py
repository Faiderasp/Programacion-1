#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PARCIAL 2 - SISTEMA BIBLIOTECA
Estudiante: Faider Asprilla Torres
Fecha: 20/10/2025
"""

from datetime import datetime, timedelta


# ===========================================================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================================================
class ErrorBiblioteca(Exception):
    """Clase base para los errores del sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    def __init__(self, isbn):
        super().__init__(f"No se encontró ningún libro con ISBN {isbn}")
        self.isbn = isbn


class LibroNoDisponible(ErrorBiblioteca):
    def __init__(self, isbn, titulo):
        super().__init__(f"'{titulo}' (ISBN {isbn}) no tiene copias disponibles")
        self.isbn = isbn
        self.titulo = titulo


class UsuarioNoRegistrado(ErrorBiblioteca):
    def __init__(self, id_usuario):
        super().__init__(f"El usuario con ID {id_usuario} no está registrado")
        self.id_usuario = id_usuario


class LimitePrestamosExcedido(ErrorBiblioteca):
    def __init__(self, id_usuario, limite):
        super().__init__(f"Usuario {id_usuario} ha superado el límite de {limite} préstamos")
        self.id_usuario = id_usuario
        self.limite = limite


class PrestamoVencido(ErrorBiblioteca):
    def __init__(self, id_prestamo, dias):
        super().__init__(f"El préstamo {id_prestamo} tiene un retraso de {dias} días")
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias


# ===========================================================================
# CLASE PRINCIPAL
# ===========================================================================
class SistemaBiblioteca:
    """
    Sistema principal para la gestión de libros, usuarios y préstamos.
    Permite registrar usuarios, administrar préstamos y generar reportes.
    """

    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos
        self._contador = 0

    # ===================== LIBROS =====================

    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        """Agrega un libro al catálogo si cumple todas las validaciones necesarias."""
        if not (isinstance(isbn, str) and isbn.isdigit() and len(isbn) == 13):
            raise ValueError("El ISBN debe tener 13 dígitos numéricos")
        if isbn in self.catalogo:
            raise KeyError(f"El ISBN {isbn} ya está registrado")
        if not titulo.strip() or not autor.strip():
            raise ValueError("El título y autor no pueden estar vacíos")
        if anio < 1000 or anio > datetime.now().year:
            raise ValueError("El año del libro no es válido")
        if copias < 1:
            raise ValueError("Debe existir al menos una copia del libro")

        self.catalogo[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "anio": anio,
            "categoria": categoria,
            "copias_total": int(copias),
            "copias_disponibles": int(copias),
            "prestamos_totales": 0
        }

    def actualizar_copias(self, isbn, cambio):
        """Modifica el número de copias disponibles y totales."""
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)

        libro = self.catalogo[isbn]
        nuevo_total = libro["copias_total"] + cambio
        nuevo_disp = libro["copias_disponibles"] + cambio

        if nuevo_total < 0 or nuevo_disp < 0:
            raise ValueError("Las copias no pueden quedar negativas")

        libro["copias_total"] = nuevo_total
        libro["copias_disponibles"] = nuevo_disp

    def buscar_libros(self, criterio="titulo", valor="", categoria=None):
        """Busca libros que coincidan con un criterio y categoría opcional."""
        resultados = []
        valor = valor.lower()

        for isbn, info in self.catalogo.items():
            if categoria and info["categoria"].lower() != categoria.lower():
                continue
            campo = str(info.get(criterio, "")).lower()
            if valor in campo:
                registro = dict(info)
                registro["isbn"] = isbn
                resultados.append(registro)
        return resultados

    # ===================== USUARIOS =====================

    def registrar_usuario(self, id_usuario, nombre, email):
        """Agrega un nuevo usuario al sistema si el ID es único y los datos válidos."""
        if id_usuario in self.usuarios:
            raise ValueError("Ya existe un usuario con ese ID")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if "@" not in email or "." not in email:
            raise ValueError("Correo electrónico inválido")

        self.usuarios[id_usuario] = {
            "nombre": nombre,
            "email": email,
            "fecha_registro": datetime.now(),
            "prestamos_activos": [],
            "historial": [],
            "multas_pendientes": 0.0
        }

    def obtener_estado_usuario(self, id_usuario):
        """Devuelve un resumen del estado actual del usuario."""
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)

        datos = self.usuarios[id_usuario]
        puede_prestar = (
            len(datos["prestamos_activos"]) < self.limite_prestamos and
            datos["multas_pendientes"] <= 50
        )

        return {
            "nombre": datos["nombre"],
            "prestamos_activos": len(datos["prestamos_activos"]),
            "puede_prestar": puede_prestar,
            "multas_pendientes": datos["multas_pendientes"]
        }

    # ===================== PRÉSTAMOS =====================

    def prestar_libro(self, isbn, id_usuario):
        """Crea un préstamo si el libro y usuario existen y cumple las condiciones."""
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)

        usuario = self.usuarios[id_usuario]
        libro = self.catalogo[isbn]

        if libro["copias_disponibles"] <= 0:
            raise LibroNoDisponible(isbn, libro["titulo"])
        if len(usuario["prestamos_activos"]) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)
        if usuario["multas_pendientes"] > 50:
            raise ValueError("El usuario tiene multas pendientes superiores al límite permitido")

        self._contador += 1
        id_prestamo = f"P{self._contador:04d}"
        fecha_inicio = datetime.now()
        fecha_vencimiento = fecha_inicio + timedelta(days=self.dias_prestamo)

        self.prestamos[id_prestamo] = {
            "isbn": isbn,
            "id_usuario": id_usuario,
            "fecha_prestamo": fecha_inicio,
            "fecha_vencimiento": fecha_vencimiento,
            "fecha_devolucion": None,
            "multa": 0.0
        }

        usuario["prestamos_activos"].append(id_prestamo)
        libro["copias_disponibles"] -= 1
        libro["prestamos_totales"] += 1

        return id_prestamo

    def devolver_libro(self, id_prestamo):
        """Gestiona la devolución de un libro, calculando multa si hay retraso."""
        if id_prestamo not in self.prestamos:
            raise KeyError("El préstamo no existe")
        prestamo = self.prestamos[id_prestamo]
        if prestamo["fecha_devolucion"] is not None:
            raise ValueError("Este préstamo ya fue devuelto")

        hoy = datetime.now()
        dias_retraso = max(0, (hoy - prestamo["fecha_vencimiento"]).days)
        multa = dias_retraso * self.multa_por_dia

        prestamo["fecha_devolucion"] = hoy
        prestamo["multa"] = multa

        usuario = self.usuarios[prestamo["id_usuario"]]
        libro = self.catalogo[prestamo["isbn"]]

        libro["copias_disponibles"] += 1
        usuario["prestamos_activos"].remove(id_prestamo)
        usuario["historial"].append(id_prestamo)
        usuario["multas_pendientes"] += multa

        mensaje = "Devolución completada" if multa == 0 else f"Multa aplicada: ${multa:.2f}"
        return {"dias_retraso": dias_retraso, "multa": multa, "mensaje": mensaje}

    def renovar_prestamo(self, id_prestamo):
        """Extiende el tiempo de un préstamo, si aún no está vencido."""
        if id_prestamo not in self.prestamos:
            raise KeyError("No existe ese préstamo")
        prestamo = self.prestamos[id_prestamo]

        if datetime.now() > prestamo["fecha_vencimiento"]:
            dias = (datetime.now() - prestamo["fecha_vencimiento"]).days
            raise PrestamoVencido(id_prestamo, dias)

        prestamo["fecha_vencimiento"] += timedelta(days=self.dias_prestamo)
        return f"El préstamo {id_prestamo} fue renovado hasta {prestamo['fecha_vencimiento'].date()}"

    # ===================== REPORTES =====================

    def libros_mas_prestados(self, n=10):
        """Retorna los libros con más préstamos registrados."""
        lista = [(isbn, info["titulo"], info["prestamos_totales"]) for isbn, info in self.catalogo.items()]
        lista_ordenada = sorted(lista, key=lambda x: x[2], reverse=True)
        return lista_ordenada[:n]

    def usuarios_mas_activos(self, n=5):
        """Retorna los usuarios con mayor cantidad de préstamos históricos."""
        lista = [(uid, u["nombre"], len(u["historial"])) for uid, u in self.usuarios.items()]
        lista_ordenada = sorted(lista, key=lambda x: x[2], reverse=True)
        return lista_ordenada[:n]

    def estadisticas_categoria(self, categoria):
        """Genera estadísticas generales sobre una categoría de libros."""
        libros_cat = {i: d for i, d in self.catalogo.items() if d["categoria"].lower() == categoria.lower()}
        if not libros_cat:
            return {}

        total_libros = len(libros_cat)
        total_copias = sum(l["copias_total"] for l in libros_cat.values())
        copias_prestadas = sum(l["copias_total"] - l["copias_disponibles"] for l in libros_cat.values())
        tasa = (copias_prestadas / total_copias) * 100 if total_copias else 0
        mas_popular = max(libros_cat.values(), key=lambda x: x["prestamos_totales"])["titulo"]

        return {
            "total_libros": total_libros,
            "total_copias": total_copias,
            "copias_prestadas": copias_prestadas,
            "tasa_prestamo": round(tasa, 2),
            "libro_mas_popular": mas_popular
        }

    def prestamos_vencidos(self):
        """Lista los préstamos que ya deberían haberse devuelto."""
        hoy = datetime.now()
        vencidos = []
        for pid, prestamo in self.prestamos.items():
            if prestamo["fecha_devolucion"] is None and prestamo["fecha_vencimiento"] < hoy:
                dias = (hoy - prestamo["fecha_vencimiento"]).days
                multa = dias * self.multa_por_dia
                libro = self.catalogo[prestamo["isbn"]]
                vencidos.append({
                    "id_prestamo": pid,
                    "isbn": prestamo["isbn"],
                    "titulo": libro["titulo"],
                    "id_usuario": prestamo["id_usuario"],
                    "dias_retraso": dias,
                    "multa_acumulada": multa
                })
        return vencidos

    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        """Calcula un resumen de las multas generadas, pagadas y pendientes."""
        total_multas = 0
        prestamos_multados = 0

        for p in self.prestamos.values():
            if p["multa"] > 0:
                fecha_referencia = p["fecha_devolucion"] or p["fecha_prestamo"]
                if (fecha_inicio and fecha_referencia < fecha_inicio) or (fecha_fin and fecha_referencia > fecha_fin):
                    continue
                prestamos_multados += 1
                total_multas += p["multa"]

        pendientes = sum(u["multas_pendientes"] for u in self.usuarios.values())
        pagadas = max(0, total_multas - pendientes)
        promedio = round(total_multas / prestamos_multados, 2) if prestamos_multados else 0

        return {
            "total_multas": round(total_multas, 2),
            "multas_pagadas": round(pagadas, 2),
            "multas_pendientes": round(pendientes, 2),
            "prestamos_con_multa": prestamos_multados,
            "promedio_multa": promedio
        }

    # ===================== ARCHIVOS =====================

    def exportar_catalogo(self, archivo="catalogo.txt"):
        """Guarda el catálogo actual en un archivo de texto plano."""
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                for isbn, info in self.catalogo.items():
                    linea = f"{isbn}|{info['titulo']}|{info['autor']}|{info['anio']}|{info['categoria']}|{info['copias_total']}\n"
                    f.write(linea)
        except Exception as e:
            print(f"Error al exportar: {e}")

    def importar_catalogo(self, archivo="catalogo.txt"):
        """Carga un catálogo desde un archivo, validando línea a línea."""
        exitos = 0
        errores = []
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for i, linea in enumerate(f, start=1):
                    try:
                        isbn, titulo, autor, anio, categoria, copias = linea.strip().split("|")
                        if isbn in self.catalogo:
                            raise ValueError("ISBN repetido")
                        self.agregar_libro(isbn, titulo, autor, int(anio), categoria, int(copias))
                        exitos += 1
                    except Exception as e:
                        errores.append((i, str(e)))
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no existe.")
        return {"exitosos": exitos, "errores": errores}


# ===========================================================================
# PRUEBAS BÁSICAS
# ===========================================================================
if __name__ == "__main__":
    print("=" * 70)
    print(" PRUEBAS DEL SISTEMA DE BIBLIOTECA ")
    print("=" * 70)

    sistema = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0)

    sistema.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    sistema.registrar_usuario("U001", "Ana García", "ana@email.com")

    prestamo_id = sistema.prestar_libro("9780134685991", "U001")
    print("Préstamo:", prestamo_id)

    sistema.prestamos[prestamo_id]["fecha_vencimiento"] = datetime.now() - timedelta(days=3)
    resultado = sistema.devolver_libro(prestamo_id)
    print("Resultado devolución:", resultado)

    print("Reporte financiero:", sistema.reporte_financiero())
