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
    result = []
    for i in range (0, n+1, 100):
        lista = []
        for j in range(i,0,-1):
            lista.append(j)
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
