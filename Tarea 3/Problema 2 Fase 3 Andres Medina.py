#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213022_230
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia

# Problema 2: Matriz que almacena números de 5 x 5 

print(" Bienvenido al programa de la matriz 5x5")
print("Con este programa se permitirá la suma y promedio del borde de una matriz 5x5")

matriz = [] 

for fila in range(5):
    fila_matriz = []
    for columna in range(5):
        while True:
            try:
                valor = int(input(f"Ingrese un número entre 10 y 90 para la posición [{fila+1},{columna+1}]: "))
                if 10 <= valor <= 90:
                    fila_matriz.append(valor)
                    break
                else:
                    print("Error: El número debe estar entre 10 y 90.")
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
    matriz.append(fila_matriz)


sumadelborde = 0
contadordelborde = 0

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            sumadelborde += matriz[i][j]
            contadordelborde += 1

promedio_borde = sumadelborde / contadordelborde

print("-----------------------------------------")
print("MATRIZ GENERADA (5x5)")

for fila in matriz:
    for elemento in fila:
        print(f"{elemento:4}", end=" ")
print() 

print("------------------------------------------")
print(f"Suma de los valores del borde: {sumadelborde}")
print(f"Promedio de los valores del borde: {promedio_borde:.2f}")
print("------------------------------------------")

print("Fin del programa. Gracias por utilizarlo.")