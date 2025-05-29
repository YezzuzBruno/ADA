import sys
import json
import random

def generar_arreglos_best_case(n):
    result=[]
    for i in range (0, n+1, 100):
        lista = []
        for j in range(1, i+1):
            lista.append(j)
        result.append(lista)
    return result


def generar_arreglos_worst_case(n):
    """Genera arreglos que maximizan comparaciones en Merge Sort"""
    result = []
    for i in range(0, n+1, 100):
        # Crear un arreglo que fuerce el máximo número de comparaciones
        lista = []
        mitad = i // 2
        for j in range(1, mitad + 1):
            lista.append(j)
            lista.append(j + mitad)
        if i % 2 != 0:  # Si es impar, agregar el último elemento
            lista.append(i)
        result.append(lista)
    return result

def generar_arreglos_average_case(n):
    result = []
    for i in range(0,n+1,100):
        lista = []
        for j in range(0, i):
            lista.append(random.randint(1,n))
        result.append(lista)
    return result

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(json.dumps({"tipo": "Mejor Caso", "datos": generar_arreglos_best_case(n), "tam": n}))
    print(json.dumps({"tipo":"Peor Caso", "datos": generar_arreglos_worst_case(n), "tam": n}))
    print(json.dumps({"tipo": "Caso Promedio", "datos": generar_arreglos_average_case(n), "tam": n}))
