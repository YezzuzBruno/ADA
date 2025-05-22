import sys
import json

def generar_arreglos_worst_case(n):
    result = []
    for i in range (0, n, 10):
        lista = []
        for j in range(i,-1,-1):
            lista.append(j+1)
        print(json.dumps(lista))

if __name__ == "__main__":
    n = int(sys.argv[1])
    generar_arreglos_worst_case(n);
