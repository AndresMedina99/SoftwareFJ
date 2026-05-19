#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213022_230
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia

#Ejerciocio 5 crear programa para polizas de seguro

def menu():
    print("SEGUROS OFICIAL S.A.")
    print("1. Hacer un pago")
    print("2. Salir")
    opcion = int(input("¿Cuál es su opción?: "))

    while opcion < 1 or opcion > 2:
        opcion = int(input("ERROR. Opción válida (1-2): "))
    return opcion


def validar_codigo(codigo):
    codigo_str = str(codigo)


    if len(codigo_str) != 7:
        return 0


    if codigo_str[0] not in ['1', '2', '3']:
        return 0

    return 1  


def calcular_pago(codigo, monto):
    tipo = int(str(codigo)[0]) 

    if tipo == 1:
        return monto
    
    elif tipo == 2:
        if monto <= 1_000_000:
            return monto  
        else:
            extra = monto - 1_000_000
            return 1_000_000 + (extra * 0.70)

    elif tipo == 3: 
        return monto * 0.65 

def main():
    polizas_validas = 0
    total_pagado = 0

    while True:
        op = menu()

        if op == 1:
            codigo = input("Digite el código de la póliza (7 dígitos): ")

            if validar_codigo(codigo) == 1:
                polizas_validas += 1
                monto = float(input("Digite el monto a pagar: "))

                valor = calcular_pago(codigo, monto)
                total_pagado += valor

                print(f"Pago realizado")
                print(f"Tipo de póliza: {codigo[0]}")
                print(f"Valor pagado por la empresa: {valor}")

            else:
                print("Código inválido. No se puede procesar el pago.")

        elif op == 2:
            break

    print("RESUMEN DEL DÍA")
    print(f"Pólizas válidas atendidas: {polizas_validas}")
    print(f"Monto pagado por la empresa: {total_pagado}")

main()
