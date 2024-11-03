import string
from collections import Counter

def contar_texto(texto):
    signos_de_puntuacion = string.punctuation + "“”‘’"
    texto_sin_puntuacion = texto.translate(str.maketrans("", "", signos_de_puntuacion))
    
    palabras = texto_sin_puntuacion.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto.replace(" ", ""))
    num_oraciones = sum(texto.count(delimitador) for delimitador in '.!?')
    frecuencia_palabras = Counter(palabras)

    return num_palabras, num_caracteres, num_oraciones, frecuencia_palabras

def mostrar_resultados(num_palabras, num_caracteres, num_oraciones, frecuencia_palabras):
    print(f"\nNúmero total de palabras: {num_palabras}")
    print(f"Número total de caracteres (sin espacios): {num_caracteres}")
    print(f"Número total de oraciones: {num_oraciones}\n")
    
    print("Frecuencia de palabras:")
    for palabra, conteo in frecuencia_palabras.most_common():
        print(f"{palabra}: {conteo}")

def esperar_enter():
    input("\nPresiona Enter para continuar...")

def main():
    print("Contador de Palabras")
    while True:
        print("\nIntroduce el texto (presiona Enter dos veces para confirmar):")
        
        texto = ""
        while True:
            linea = input()
            if linea == "":
                if texto:
                    break
            else:
                texto += linea + "\n"

        num_palabras, num_caracteres, num_oraciones, frecuencia_palabras = contar_texto(texto)
        mostrar_resultados(num_palabras, num_caracteres, num_oraciones, frecuencia_palabras)

        continuar = input("\n¿Quieres contar otro texto? (s para continuar, cualquier otra tecla para salir): ")
        if continuar.lower() != 's':
            print("Saliendo del programa...")
            break

        esperar_enter()

if __name__ == "__main__":
    main()
