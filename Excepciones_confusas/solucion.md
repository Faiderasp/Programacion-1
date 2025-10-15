# Integrantes
- Faider Asprilla Torres
- Juan David Martínez González

## Problema 1: Capturar todo con except desnudo
### ¿Cómo sabrías qué salió mal en producción?
No hay manera de saberlo debido a que solo retiene el error más no indica el tipo.
### ¿Qué pasa si hay un error de tipeo en 'resultado'?
Si el error hace que no se pueda correr la función, lo retiene.
### ¿Cómo afecta esto a la depuración?
Lo afecta de manera negativa, debido a que, a pesar de que el programa no se detiene, no podemos saber qué corregir.

## Problema 2: Capturar demasiado ampliamente:
### ¿Cuál es el problema aquí?
Los problemas al que se podría exponer el código son: 
- invalid literal.
- división por cero.
Si no se hace un buen manejo.
#### ¿Deberían manejarse todos de la misma manera?
No, porque pueden haber errores por palabras en la entrada, divisiones por cero y valores invalidos.
#### ¿Qué información se pierde al capturar todo?
Se pierde el tipo de excepción, ya que se generaliza.

## Problema 3: Ignorar errores silenciosamente
### ¿El usuario sabe si guardó correctamente?
No, porque el código no muestra ningún mensaje ni confirmación.
### ¿Cómo depurarías esto si falla?
Sería complicado, ya que el error se ignora completamente. No hay registro ni aviso, así que habría que revisar el código manualmente.
### ¿Qué debería suceder cuando falla el guardado?
El programa debería avisar al usuario que el guardado falló e indicar la causa.
### ¿Cómo informarías al usuario?
    except Exception as e:
        print(f"Error al guardar configuración: {e}")
### ¿Es este error algo que deberías manejar?
Sí, pero no de forma silenciosa. Debe manejarse mostrando información útil o registrando el fallo.

## Problema 4: Confusión con else y finally
### ¿Cuándo se ejecuta cada bloque?
- El try se ejecuta normalmente en la funcionalidad, y evalua errores.
- Solo si ocurre una excepción (en este caso, ValueError).
- El else solo si NO ocurrió ningún error en el try.
- El finally funciona siempre, pase lo que pase.
#### ¿En qué se diferencia else de finally?
El else va enlazado al 'if' en cambio el finally siempre ocurre al acabar una sentencia de código.
#### ¿Cuándo usarías cada uno?
El finally cuando quiero que algo se ejecute sin importa qué, en cambio el else, cuando lo tengo sujeto a una condición.

## Problema 5: Uso incorrecto de raise
### ¿Qué está mal con estos usos de raise?
Se usan excepciones genéricas y mensajes poco claros, lo que dificulta entender el tipo de error y complica el manejo de errores.
### ¿Qué tipo de excepción sería más apropiado?
Depende del caso, podemos simplemente recibir el tipo de error y mostrarlo, o si queremos ser más especificos, buscar el tipo de error y hacer un catch para cada uno.
### ¿Qué información debería incluir el mensaje?
El mensaje debe ser específico y explicar claramente qué salió mal y por qué.
### ¿Cómo ayuda esto a quien llama la función?
Le permite manejar los errores adecuadamente con try-except y comprender rápidamente el origen del fallo.

# Problema 6: No re-lanzar excepciones apropiadamente
### ¿Deberías siempre capturar y consumir errores?
Sí, para el sano y eficaz funcionamiento del software, primordialmente si está en el ambiente de producción.
#### ¿Qué pasa si el llamador necesita saber que falló?
En tal caso, se debería manejar el error de una manera diferente, en la cual se pueda mostrar el error.
#### ¿Deberías siempre manejar el error localmente?
Solo en un caso muy especifico se debería manejar el error de forma local.
#### ¿Cuándo deberías capturar y manejar?
Se debería manejar necesito hacer algún manejo de errores, o gestionar algo con ello. Y capturar, cuando es un error concurrente y no es muy relevante en la funcionalidad.
#### ¿Cuándo deberías capturar, registrar y re-lanzar?
Y capturar, cuando es un error concurrente y no es muy relevante en la funcionalidad. Se registra, cuando se quiere tener un historial de los errores que han estado en la app y se hace un relanzamiento cuando se quiere hacer varias de las pruebas de la funcionalidad.
#### ¿Cuándo NO deberías capturar en absoluto?
Cuando no es necesario en la funcionalidad y en cambio, la entorpece.

## Problema 7: Manejo de excepciones en bucles
### ¿Qué pasa cuando una excepción ocurre en un bucle?
Si no se maneja, se detiene el bucle, lo que podría causar fallas en el programa debido a que no se ejecutó la cantidad de veces necesarias.
### ¿Qué pasa si un elemento causa error?
El programa se interrumpe justo en ese punto y no continúa con los demás elementos.
### ¿Debería un error detener todo el proceso?
Depende del caso, pero normalmente no. Lo ideal es continuar con los demás elementos.
### ¿Cómo reportarías múltiples errores?
Podría hacerse guardando cada error en una lista que nos sirva como log para revisar después.
### ¿Qué pasa si TODOS los elementos fallan?
Debería informarse del error de cada elemento, con el objetivo de arreglarlos antes de volver a ejecutar el programa.