# Ejercicio 1.1

print(5 + 3 * 2)

# Mi prediccion: 11
# Resultado: 11
# Explicación: se opera primero 3*2 lo cual da 6 y luego se suma el 5, dando como resultado 11.
# Ejercicio 1.2

print((5 + 3) * 2)

# Mi prediccion: 16
# Resultado: 16
# Explicación: Se opera primero lo que está dentro del parentesis, 
# 5 + 3, lo cual da 8, y posteriormente se multiplica por 2, dando como resultado 16.

# Ejercicio 1.3

print(10 / 2)
print(10 // 2)
print(10 % 2)

# Mis predicciones: 
# 5.0, resultado: 5.0
# 5, resultado: 5
# 0, resultado: 0.

# Ejercicio 1.4

print(2 ** 3)
print(2 ^ 3)

# Mis predicciones: 
# 8, resultado: 8
# 1, resultado: 1.
# Explicación: El primero expresa 2 elevado al cubo, 
# el segundo hace una operación XOR bit a bit entre los dos números.

# Ejercicio 1.5

print(5 - -3)
print(-5 * -3)

# Mis predicciones: 
# 8, resultado: 8
# 15, resultado: 15.
# Explicación: En el primero, se se hace la operación 5 - (-3) y por propiedades de los signos da 8,
# El segundo, por ley de signos, da 15.

## Expresiones Complejas

# Ejercicio 2.1

print(2 + 3 * 4 - 5)

# Mi predicción: 9.

# Ejercicios 2.2

print(20 / 4 * 2)
print(20 / (4 * 2))

# Mis predicciones: 
# 10.0, resultado: 10.0
# 2.5, resultado: 2.5.

# Ejercicio 2.3

print(17 % 5 + 2 * 3)

# Mi predicción: 8, resultado: 8.

# Ejercicio 2.4

print(2 ** 3 ** 2)
print((2 ** 3) ** 2)

# Tus predicciones: 
# 512, resultado: 512
# 64, resultado: 64.

# Ejercicio 2.5

print(10 + 5 * 2 - 8 / 4 + 3)

# Mi predicción: 21.0, resultado: 21.0.

## Problemas del Mundo Real

# Ejercicio 3.1

# Calcula el total con impuesto del 15% sobre una compra de $100.

price = 100
tax_rate = 0.15

# Expresión correcta:

total = price * (1 + tax_rate)

# Ejercicio 3.2

# Convierte 25°C a Fahrenheit usando la fórmula: F = (C × 9/5) + 32

celsius = 25

# Expresión:

Fahrenheit = (celsius * 9 / 5) + 32

# Ejercicio 3.3

# Calcula el promedio de 3 calificaciones: 85, 90, 78

grade1 = 85
grade2 = 90
grade3 = 78

# Expresión correcta:

average = (grade1 + grade2 + grade3) / 3

# Ejercicio 3.4

# 4 amigos van a cenar. La cuenta es $127.50. Calcula cuánto paga cada uno.

total_bill = 127.50
num_people = 4

# Cálculo:

per_person = total_bill / num_people

# Ejercicio 3.5
# Tienes 125 minutos. ¿Cuántas horas y minutos son?

total_minutes = 125

# Horas
hours = total_minutes // 60

# Minutos
minutes = total_minutes % 60

## Proyecto Final

# Tu código aquí

expression = input("Ingresa una expresión: ")

# Evaluar y mostrar resultado
# Manejar división por cero
# Manejar expresiones inválidas

#Librería para el tipado
from typing import List,Tuple,Any

def calculadora_expresiones(expression: str):
    print("=== CALCULADORA DE EXPRESIONES ===")
    historial = List[tuple[str,Any]]
    while True:
        print("="*20)
        expression = input("Ingresa una expresión ('historial' para ver el historial o 'salir' para terminar): ")
        print("Operadores: +, -, *, /, //, %, **")
        if expression.lower() == 'salir':
            print("\nMuchas gracias!!!")
            print("="*20)
            break
        elif expression.lower() == 'historial':
            if historial:
                for i,u in enumerate(historial):
                    print("\n=== HISTORIAL ===")
                    print(f"Expresion: {u[0]}, resultado: {u[1]}")
            else:
                print("\nHistorial vacío.\n")
            continue
        else:
            try:
                operacion = eval(expression)
                print(f"Resultado: {operacion}")
                print(f"Tipo: {type(operacion).__name__}")
                historial.append(tuple(expression,operacion))
            except ZeroDivisionError:
                print("Error: División por cero")
            except SyntaxError:
                print("Error: Sintaxis inválida")
            except NameError:
                print("Error: Variable no definida")
            except:
                print("Error: Desconocido")

# Ejercicios de Debugging

# Debug 1

# Este código debería calcular el promedio

a = 10
b = 20
c = 30
average = a + b + c / 3

# ¿Qué está mal?: Los 3 valores deberían estar en paréntesis, porque si no solo divide c por 3

print(f"Promedio: {average}")

# Debug 2

# Calcular 20% de descuento sobre $50
price = 50
discount = 20
final = price - discount * price
print(f"Precio final: ${final}")

# ¿Qué está mal?:Se está multiplicando el descuento por el precio "20 * 50 = 1000"
