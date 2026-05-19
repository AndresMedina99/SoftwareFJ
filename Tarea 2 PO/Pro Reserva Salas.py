#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213023_154
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia

# Construcción de la clase ReservaSala

class ReservaSala:
    def __init__(self, usuario, tarifa_hora):
        self._usuario = usuario
        self._hora_inicio = None
        self._tarifa_hora = tarifa_hora

    #Proceso para guardar la reserva (Método registrar_inicio(hora) )

    def registrar_inicio(self, hora):
        if hora < 0 or hora > 24:
            print("Hora de inicio invalida")
        else:
            self._hora_inicio = hora
            print("Hora de inicio registrada")

    # Proceso para validar la hora final de la reserva
    def registrar_fin(self, hora):
        if self._hora_inicio is None:
            print("Primero debe registrar la hora de inicio")
            return None

        if hora <= self._hora_inicio or hora > 24:
            print("Hora de fin invalida")
            return None

        return hora

    # Proceso para generar el costo de la reserva ( Calcular Costo)
    def calcular_costo(self, hora_fin):
        if self._hora_inicio is None:
            print("No hay hora de inicio registrada")
            return 0


        horas = hora_fin - self._hora_inicio
        costo = horas * self._tarifa_hora

        return costo
    
    #Metodo para obtener el usuario de la reserva

    def obtener_usuario(self):
        return self._usuario


reservas = []


# Menú principal
while True:
    print("Sistema de reservas")
    print("1. Crear reserva")
    print("2. Finalizar reserva")
    print("3. Ver reservas")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    # creación de la reserva
    if opcion == "1":
        usuario = input("Ingrese el nombre del usuario: ")

        try:
            tarifa = float(input("Ingrese la tarifa por hora: "))
        except:
            print("Dato invalido")
            continue

        reserva = ReservaSala(usuario, tarifa)

        try:
            hora_inicio = float(input("Ingrese la hora de inicio (0-24): "))
        except:
            print("Hora invalida")
            continue

        reserva.registrar_inicio(hora_inicio)
        reservas.append(reserva)

        print("Reserva creada")

    # Proceso para Finalizar una reserva
    elif opcion == "2":
        if len(reservas) == 0:
            print("No hay reservas registradas")
            continue

        print("Reservas disponibles:")
        for i, r in enumerate(reservas):
            print(i, "-", r.obtener_usuario())

        try:
            indice = int(input("Seleccione una reserva: "))
            reserva = reservas[indice]
        except:
            print("Seleccion invalida")
            continue

        try:
            hora_fin = float(input("Ingrese la hora de fin (0-24): "))
        except:
            print("Hora invalida")
            continue

        hora_valida = reserva.registrar_fin(hora_fin)

        if hora_valida is not None:
            costo = reserva.calcular_costo(hora_valida)
            print("Costo total:", costo)

    # Reservas que se han realizado
    elif opcion == "3":
        if len(reservas) == 0:
            print("No hay reservas")
        else:
            for i, r in enumerate(reservas):
                print(i, "-", r.obtener_usuario())

    elif opcion == "4":
        print("Fin del programa")
        break

    else:
        print("Opcion invalida")
        