import pprint as pp
def juegoAyB(frase: str):
    cadenaA = {}
    cadenaB = {}
    for i, letra in enumerate(frase.lower()):
        if letra in "aeiou":
            frase_vocal = ""
            for n in range(i, len(frase)):
                frase_vocal += frase[n]
                cadenaA[frase_vocal] = cadenaA.get(frase_vocal, 0) + 1
        else:
            frase_consonante = ""
            for j in range(i, len(frase)):
                frase_consonante += frase[j]
                cadenaB[frase_consonante] = cadenaB.get(frase_consonante, 0) + 1

    return cadenaA,cadenaB
a = sum([u for u in juegoAyB("murcielago")[0].values()])
b = sum([u for u in juegoAyB("murcielago")[1].values()])
print(f"Ganador B con {b} -> {juegoAyB("murcielago")[1]}" if b > a else f"Ganador A con {a} -> {juegoAyB("murcielago")[1]}")