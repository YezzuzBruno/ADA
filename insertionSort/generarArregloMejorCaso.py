import sys
import json

def generar_arreglos_best_case(n):
    for i in range (0, n+1, 100):
        lista = []
        for j in range(1, i+1):
            lista.append(j)
        print(json.dumps(lista))

if __name__ == "__main__":
    n = int(sys.argv[1])
    generar_arreglos_best_case(n);
