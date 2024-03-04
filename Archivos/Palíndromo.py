'''
Escribir una función que reciba un texto (string)
Esta función debe devolver TRUE en caso sea un palíndromo
Y FALSE en caso que no lo sea
'''


def palindromo(nombre: str):
    nombre = nombre.replace(" ", "").lower()
    return nombre == nombre[::-1]


print(palindromo(input("Ingrese la palabra a verificar => ")))
