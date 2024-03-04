lista = [3, 5, 11, 1, 2, 8, 22, 13, 15, 4, 6, 16, 25]
lista.sort()
print(lista)

def busqueda_bin(valor):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        puntero = (inicio + final) // 2

        if valor == lista[puntero]:
            return puntero
        
        elif valor > lista[puntero]:
            inicio = puntero + 1

        else:
            final = puntero - 1
    
    return None

def busqueda(valor):
    resultado = busqueda_bin(valor)

    if resultado is None:
        print(f"El número {valor} no se encuentra en la lista")

    else:
        print(f"El número {valor} se encuentra en la posición {resultado}")

busqueda(8)