'''
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
'''

def escalera(pasos: int):
    if pasos > 0:
        for paso in range(pasos + 1): #se suma uno por porque en la interación no cuenta al último 
            espacios = "  " * (pasos - paso) 
            dibujo_paso = "_" if paso == 0 else "_|"
            print(f"{espacios}{dibujo_paso}")

    if pasos < 0:
        for paso in range(abs(pasos) + 1): #"abs" para considerar su valor absoluto (no negativo) 
            espacios = " " * ((paso * 2) - 1) # -1 es cuando se itere con 1 solamente se considere un espacio
            dibujo_paso = "_" if paso == 0 else "|_"
            print(f"{espacios}{dibujo_paso}")

escalera(-9)
escalera(9)