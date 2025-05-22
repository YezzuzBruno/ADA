import sys
import json
import time

def merge_sort(arr):
    # Si el arreglo tiene 1 o menos elementos, ya está ordenado
    if len(arr) <= 1:
        return arr
    
    medio = len(arr) // 2  # Dividir el arreglo en dos mitades
    izquierda = merge_sort(arr[:medio])  # Llamada recursiva para la mitad izquierda
    derecha = merge_sort(arr[medio:])   # Llamada recursiva para la mitad derecha

    # Llamar a la función merge para combinar las dos mitades ordenadas
    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []  # Lista para almacenar el arreglo ordenado
    i = j = 0  # Punteros para las listas izquierda y derecha

    # Comparar los elementos de ambas listas y agregar el menor al resultado
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # Añadir los elementos que quedan en la lista izquierda o derecha
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

def calcular_tiempos():
    for linea in sys.stdin:
        arreglo = json.loads(linea)
        inicio = time.time()
        merge_sort(arreglo)
        fin = time.time()
        tiempo = fin - inicio
        print(json.dumps({
            "tam" : len(arreglo),
            "time" : tiempo
        }))


if __name__ == "__main__":
    calcular_tiempos()
