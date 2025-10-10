### Ejercicio 1.1: Predice los Resultados

print(True and False) # False
print(True or False) # True
print(not True) # False
print(not False) # True

# Tus predicciones: False, True, False, True;

### Ejercicio 1.2: Operadores Combinados

a, b, c = True, False, True

print(a and b)  # False
print(a or b)   # True
print(b or c)   # True
print(a and c)  # True

# Tus predicciones: False, True, True, True;

### Ejercicio 1.3: Precedencia

a, b, c = True, False, True

print(a and b or c)      # True
print(a or b and c)      # True
print(not a or b)        # False
print(not (a or b))      # False

# Tus predicciones: True, True, False, False;

### Ejercicio 1.4: Comparaciones y Lógica

x = 5
print(x > 3 and x < 10)  # True
print(x < 3 or x > 10)   # False
print(not x > 3)         # False

# Tus predicciones: True, False, False;

### Ejercicio 1.5: Comparaciones Encadenadas

x = 5
print(3 < x < 10)        # True
print(1 <= x <= 3)       # False
print(10 > x > 3)        # True
# Tus predicciones: True, False, True;

### Ejercicio 2.1: Valores Retornados

print("hola" and "mundo")  # mundo
print("hola" and "")       # ""
print("" and "mundo")      # ""
print("hola" or "mundo")   # "hola"
print("" or "mundo") # "mundo"

# Tus predicciones: "mundo", "", "", "hola", "mundo";
### Ejercicio 2.2: Truthy y Falsy

print(bool(0))          # False
print(bool(""))         # False
print(bool([]))         # False
print(bool([0]))        # True
print(bool(" "))        # True
print(bool(None))       # False

# Tus predicciones: False, False, False, True, True, False;

### Ejercicio 2.3: Evaluación de Cortocircuito

def f1():
    print("f1 ejecutada")
    return True

def f2():
    print("f2 ejecutada")
    return False

# Caso 1
print("Caso 1:")
resultado = f1() and f2()
print(f"Resultado: {resultado}")
# Tu predicción: False

# Caso 2
print("\nCaso 2:")
resultado = f2() and f1()
print(f"Resultado: {resultado}")
# Tu predicción: False

# Caso 3
print("\nCaso 3:")
resultado = f1() or f2()
print(f"Resultado: {resultado}")
# Tu predicción: True

# Tus predicciones: False, False, True;
### Ejercicio 2.4: Operadores de Pertenencia

nums = [1, 2, 3, 4, 5]
print(3 in nums)        # True
print(6 in nums)        # False
print(6 not in nums)    # True

word = "Python"
print("P" in word)      # True
print("p" in word)      # False
print("th" in word)     # True

# Tus precciones: True, False, True, True, False, True;

### Ejercicio 2.5: Identidad vs Igualdad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)  # True
print(lista1 is lista2)  # False
print(lista1 == lista3)  # True
print(lista1 is lista3)  # True
# Tus predicciones: True, False, True, True;

### Ejercicio 3.1: Validación de Formulario
# Implementa la función `validar_datos` que verifica si:
# - El nombre tiene entre 2 y 30 caracteres
# - El email contiene '@'
# - La edad es mayor o igual a 18
# - La contraseña tiene al menos 8 caracteres

def validar_datos(nombre, email, edad, password):
    import re
    email_model = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if email and password and edad and nombre:
        if re.match(email_model,email) and len(nombre) > 2 and edad >= 18 and len(password) >= 8:
            return True
    return False

            

# Pruebas
print(validar_datos("Ana", "ana@email.com", 25, "secreto123"))  # Debe ser True
print(validar_datos("", "no-email", 15, "123"))  # Debe ser False

### Ejercicio 3.2: Sistema de Autorización

def puede_acceder(usuario, permiso_requerido, lista_negra):
    return True if (usuario["autenticado"] and (usuario["admin"] or permiso_requerido in usuario["permisos"]) and usuario["id"] not in lista_negra) else False

# Usuario ejemplo
admin = {
    "id": 1,
    "autenticado": True,
    "admin": True,
    "permisos": ["leer", "escribir"]
}

usuario_normal = {
    "id": 2,
    "autenticado": True,
    "admin": False,
    "permisos": ["leer"]
}

usuario_bloqueado = {
    "id": 3,
    "autenticado": True,
    "admin": False,
    "permisos": ["leer", "escribir"]
}

lista_negra = [3, 4]

print(puede_acceder(admin, "borrar", lista_negra))  # True
print(puede_acceder(usuario_normal, "leer", lista_negra))  # True
print(puede_acceder(usuario_normal, "escribir", lista_negra))  # False
print(puede_acceder(usuario_bloqueado, "leer", lista_negra))  # False

### Ejercicio 3.3: Acceso Seguro a Diccionario
# Implementa una función `obtener_valor_seguro` que retorne:
# - El valor de la clave si existe
# - Un valor predeterminado si la clave no existe

def obtener_valor_seguro(diccionario, clave, predeterminado=None):
    try:
        if diccionario[clave]:
            return diccionario[clave]
    except KeyError:
        return predeterminado

config = {"timeout": 30, "retries": 3}
print(obtener_valor_seguro(config, "timeout"))  # 30
print(obtener_valor_seguro(config, "cache"))  # None
print(obtener_valor_seguro(config, "cache", 60))  # 60

### Ejercicio 3.4: Filtrar Lista

def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    return [p for p in productos if precio_min <= p["precio"] <= precio_max and p["disponible"] and (categoria is None or p["categoria"] == categoria)]

productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica", "disponible": True},
    {"nombre": "Teléfono", "precio": 800, "categoria": "Electrónica", "disponible": False},
    {"nombre": "Libro", "precio": 15, "categoria": "Libros", "disponible": True},
    {"nombre": "Audífonos", "precio": 200, "categoria": "Electrónica", "disponible": True},
]

print(filtrar_productos(productos, 0, 500))
print(filtrar_productos(productos, 100, 1000, "Electrónica"))

### Ejercicio 3.5: Evaluación de Riesgo
#Implementa un sistema de evaluación de riesgo crediticio:

def evaluar_riesgo(cliente):
    """
    Evalúa si un cliente tiene bajo riesgo crediticio.
    
    Criterios:
    - Score crediticio alto (>700) O
    - Ingreso anual >50000 Y historial > 2 años O
    - Cliente VIP Y sin deudas pendientes
    """
    return True if cliente['score_crediticio'] > 700 or cliente['ingreso_anual'] > 50000\
    and cliente['años_historial'] > 2 or cliente['vip']\
    and not cliente['deudas_pendientes'] else False

cliente1 = {
    "nombre": "Ana García",
    "score_crediticio": 720,
    "ingreso_anual": 45000,
    "años_historial": 3,
    "vip": False,
    "deudas_pendientes": False
}

cliente2 = {
    "nombre": "Luis Pérez",
    "score_crediticio": 680,
    "ingreso_anual": 60000,
    "años_historial": 4,
    "vip": False,
    "deudas_pendientes": False
}

cliente3 = {
    "nombre": "Carmen Ruiz",
    "score_crediticio": 690,
    "ingreso_anual": 30000,
    "años_historial": 1,
    "vip": True,
    "deudas_pendientes": False
}

print(evaluar_riesgo(cliente1))  # True
print(evaluar_riesgo(cliente2))  # True
print(evaluar_riesgo(cliente3))  # True


### PROYECTO FINAL: Sistema de Control de Acceso

usuarios = [
    {
        "id": 1,
        "nombre": "Admin",
        "roles": ["admin"],
        "permisos": ["leer", "escribir", "eliminar"],
        "plan": "premium",
        "activo": True,
        "edad": 35
    },
    {
        "id": 2,
        "nombre": "Usuario Regular",
        "roles": ["usuario"],
        "permisos": ["leer"],
        "plan": "basico",
        "activo": True,
        "edad": 17
    },
    {
        "id": 3,
        "nombre": "Usuario Premium Adulto",
        "roles": ["usuario"],
        "permisos": ["leer", "escribir"],
        "plan": "premium",
        "activo": True,
        "edad": 25
    },
    {
        "id": 4,
        "nombre": "Usuario Inactivo",
        "roles": ["usuario"],
        "permisos": ["leer"],
        "plan": "premium",
        "activo": False,
        "edad": 30
    },
]

recursos = [
    {
        "id": 1,
        "nombre": "Panel Admin",
        "requiere_rol": ["admin"],
        "requiere_permiso": "eliminar",
        "solo_adultos": False
    },
    {
        "id": 2,
        "nombre": "Contenido Premium",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": True,
        "solo_adultos": False
    },
    {
        "id": 3,
        "nombre": "Contenido para Adultos",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": False,
        "solo_adultos": True
    },
    {
        "id": 4,
        "nombre": "Foro Público",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": False,
        "solo_adultos": False
    },
]


def puede_acceder_recurso(usuario, recurso):
    """
    Determina si un usuario puede acceder a un recurso específico.
    
    Args:
        usuario (dict): Diccionario con datos del usuario.
        recurso (dict): Diccionario con datos del recurso.
        
    Returns:
        tuple: (acceso, motivo) donde acceso es un booleano y motivo explica la decisión.
    """
    if not usuario["activo"]:
        return False, "Usuario inactivo"
    
    if "requiere_rol" in recurso:
        tiene_rol = any(rol in recurso["requiere_rol"] for rol in usuario["roles"])
        if not tiene_rol:
            return False, f"Requiere rol: {recurso['requiere_rol']}"
    
    if "requiere_permiso" in recurso and recurso["requiere_permiso"] not in usuario["permisos"]:
        return False, f"Falta permiso: {recurso['requiere_permiso']}"
    
    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return False, "Requiere plan premium"
    
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return False, "Solo para mayores de 18 años"
    
    return True, "Acceso permitido"


def probar_accesos():
    resultados = []
    for usuario in usuarios:
        print(f"\nUsuario: {usuario['nombre']} ({usuario['roles'][0]})")
        print("-" * 50)
        for recurso in recursos:
            acceso, motivo = puede_acceder_recurso(usuario, recurso)
            print(f"Recurso: {recurso['nombre']}")
            print(f"Acceso: {'PERMITIDO' if acceso else 'DENEGADO'}")
            print(f"Motivo: {motivo}\n")
            resultados.append({
                "usuario": usuario["nombre"],
                "recurso": recurso["nombre"],
                "acceso": acceso,
                "motivo": motivo
            })
    return resultados


if __name__ == "__main__":
    probar_accesos()


### Debug 1: Encuentra el Error

# Este código debería verificar si el usuario tiene permisos
def verificar_permisos(usuario, accion):
    if usuario["permisos"] and accion in usuario["permisos"]:
        return True
    else:
        return False

# Prueba
usuario = {"id": 1, "nombre": "Juan"}
print(verificar_permisos(usuario, "leer"))

# ¿Qué está mal?: El diccionario no tiene la clave ["permisos"] que estamos usando en la función.


### Debug 2: Encuentra el Error

# Este código debería filtrar estudiantes aprobados
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": None},
    {"nombre": "Carmen", "nota": 92}
]

aprobados = [e for e in estudiantes if e["nota"] >= 60]
print(aprobados)

# ¿Qué está mal?: En caso de Luis, nota es None, entonces esto ocasionaría un error al compararla con un número; debería verificar antes que no sea None.