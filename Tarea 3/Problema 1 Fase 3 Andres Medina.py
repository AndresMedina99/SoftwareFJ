#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213022_230
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia


# Problema 1: Elegir un número entre 10 y 90

print ("Programa para obtener los divisores de un número entre 10 y 90")

while True:
    try:
        numero = int (input ( " Ingrese un número entero entre 10 y 90 " ))
        if 10 <= numero <= 90:

            break
        else:
            print(" Error: El número debe estar entre 10 y 90. Intente nuevamente.")

    except ValueError:
        print (" Error: Debe ingresar un número entero.")

# Paso del calculo entre divisores y el contador de los número ingresados 
divisores = []
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
        contador += 1
print(f" Los divisores de {numero} son: {divisores}")
print(f" Cantidad total de divisores: {contador}")