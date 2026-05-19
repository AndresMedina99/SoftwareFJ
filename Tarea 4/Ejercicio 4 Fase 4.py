#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213022_230
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia

#Ejerciocio 4 crear programa para tiquetes de empresa de transpórte

def menu():
    print("VIAJES")
    print("1. Vender pasaje")
    print("2. Salir")
    opcion = int(input("¿Cuál es su opción?: "))
    return opcion

def datos():
    print("Destinos disponibles")
    print("1. Cúcuta")
    print("2. Bucaramanga")
    print("3. Bochalema")

    destino_op = int(input("Seleccione destino (1-3): "))
    while destino_op not in [1, 2, 3]:
        destino_op = int(input("ERROR. Seleccione destino válido (1-3): "))

    if destino_op == 1:
        destino = "Cúcuta"
    elif destino_op == 2:
        destino = "Bucaramanga"
    else:
        destino = "Bochalema"
    
    clase = int(input("Seleccione clase (1 Primera, 2 Segunda, 3 Tercera): "))
    while clase not in [1, 2, 3]:
        clase = int(input("ERROR. Clase válida (1-3): "))
    
    cantidad = int(input("Cantidad de pasajes: "))
    while cantidad <= 0:
        cantidad = int(input("ERROR. Digite un número positivo: "))

    return destino, clase, cantidad

def valor_pa(destino, clase):
    precios = {
        "Cúcuta": {1: 20000, 2: 15000, 3: 12000},
        "Bucaramanga": {1: 30000, 2: 25000, 3: 20000},
        "Bochalema": {1: 10000, 2: 8000, 3: 5000}
    }
    return precios[destino][clase]

def descu(cantidad):
    if cantidad < 5:
        return 0
    elif 6 <= cantidad <= 12:
        return 0.10
    else:
        return 0.20
    
def pago(cantidad, valor_base, descuento):
    subtotal = cantidad * valor_base
    total = subtotal - (subtotal * descuento)
    return total

def main():
    total_recaudo = 0
    pasajes_destino = {"Cúcuta": 0, "Bucaramanga": 0, "Bochalema": 0}

    while True:
        op = menu()

        if op == 1:
            destino, clase, cantidad = datos()
            valor_base = valor_pa(destino, clase)
            descuento = descu(cantidad)
            total = pago(cantidad, valor_base, descuento)

            pasajes_destino[destino] += cantidad
            total_recaudo += total

            print(f"Valor del pasaje: {valor_base}")
            print(f"Descuento aplicado: {descuento * 100}%")
            print(f"TOTAL A PAGAR: {total}\n")

        elif op == 2:
            break
        else:
            print("Opción no válida.")

    print("Información Final de Ventas")
    print("Pasajes vendidos:")
    for d, p in pasajes_destino.items():
        print(f"{d}: {p}")
    print(f"Total recaudado: {total_recaudo}")

main()