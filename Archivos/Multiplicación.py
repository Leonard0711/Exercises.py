

def multiplicacion(valor: int):
    for i in range(1, 13):
        resultado = i * valor
        print(f"{i} * {valor} = {resultado}")

multiplicacion(int(input("Ingrese el valor => ")))