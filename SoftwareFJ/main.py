#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213023_154
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia

from clases.cliente import Cliente
from clases.reserva import Reserva
from clases.logger import registrar_log

from clases.reserva_sala import ReservaSala
from clases.alquiler_equipo import AlquilerEquipo
from clases.asesoria import AsesoriaEspecializada

clientes = []
reservas = []

print("===== SISTEMA SOFTWARE FJ =====")

# OPERACIÓN 1

try:

    cliente1 = Cliente(
        "Andres",
        "andres@gmail.com",
        "3001234567"
    )

    clientes.append(cliente1)

    print(cliente1.mostrar_informacion())

except Exception as e:

    registrar_log(str(e))
    print("Error:", e)

# OPERACIÓN 2

try:

    cliente2 = Cliente(
        "",
        "correo_malo",
        "abc"
    )

except Exception as e:

    registrar_log(str(e))
    print("Error controlado:", e)

# OPERACIÓN 3

try:

    sala = ReservaSala("Sala VIP", 50)

    reserva1 = Reserva(cliente1, sala, 5)

    costo = reserva1.procesar_reserva()

    reservas.append(reserva1)

    print("Reserva realizada correctamente")
    print("Costo:", costo)

except Exception as e:

    registrar_log(str(e))
    print("Error:", e)

# OPERACIÓN 4

try:

    asesoria = AsesoriaEspecializada(
        "Asesoría Python",
        100
    )

    reserva2 = Reserva(cliente1, asesoria, -2)

except Exception as e:

    registrar_log(str(e))
    print("Error controlado:", e)

print("Sistema funcionando correctamente")