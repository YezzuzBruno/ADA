import time
import sys
import json

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
        entrada = json.loads(linea)
        arreglos = entrada["datos"]
        tipo = entrada["tipo"]
        tam = entrada["tam"]
        
        tiempos = []
        sizes = []
        
        for arr in arreglos:
            repeticiones = 20
            tiempo_total = 0
            size = len(arr)
            
            for _ in range(repeticiones):
                copy_array = arr.copy()
                inicio = time.perf_counter()
                copy_array = merge_sort(copy_array)
                fin = time.perf_counter()
                tiempo_total += fin - inicio
            
            tiempo_promedio = tiempo_total / repeticiones
            tiempos.append(tiempo_promedio)
            sizes.append(size)
        
        # Enviar los datos para cada tipo de caso
        print(json.dumps({
            "tipo": tipo,
            "sizes": sizes,
            "times": tiempos
        }))

if __name__ == "__main__":
    calcular_tiempos()
