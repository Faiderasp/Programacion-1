def operacion_confusa(tiene_error):
    print(f"\n[Ejecutando con tiene_error={tiene_error}]")
    try:
        print("  1. En el bloque try")
        if tiene_error:
            raise ValueError("Error simulado")
        print("  2. Try completado sin error")
    except ValueError:
        print("  2. En el bloque except")
    else:
        print("  3. En el bloque else")
    finally:
        print("  4. En el bloque finally")

operacion_confusa(True)