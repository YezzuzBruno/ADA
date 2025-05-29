import time
import sys
import json

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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
                insertion_sort(copy_array)
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
