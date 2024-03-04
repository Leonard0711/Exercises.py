
def multiplicacion(base = 1, valor = 1):
    print(f"{valor} X {base} = {valor * base}")
    if valor == 12: return
    multiplicacion(base, valor + 1)

multiplicacion(int(input("Ingresa el valor => ")))
