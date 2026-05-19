#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213023_154
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia

class Empleado:
    def __init__(self, nombre, identificacion, salario_base):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario_base = salario_base

    def calcular_salario(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        info = f"Nombre: {self.nombre} | ID: {self.identificacion}"

        if mostrar_salario:
            info += f" | Salario: {self.calcular_salario()}"

        if mostrar_detalles:
            info += " | Tipo: Empleado"

        print(info)


# ================================
# CLASES HIJAS (HERENCIA)
# ================================

# 1. Empleado tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, identificacion, salario_base, bonificacion):
        super().__init__(nombre, identificacion, salario_base)
        self.bonificacion = bonificacion

    def calcular_salario(self):
        return self.salario_base + self.bonificacion


# 2. Empleado por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, identificacion, horas_trabajadas, valor_hora):
        super().__init__(nombre, identificacion, 0)
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.valor_hora


# 3. Empleado por comisión
class EmpleadoComision(Empleado):
    def __init__(self, nombre, identificacion, salario_base, ventas, porcentaje):
        super().__init__(nombre, identificacion, salario_base)
        self.ventas = ventas
        self.porcentaje = porcentaje

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.porcentaje)


# ================================
# CLASE BONIFICABLE
# ================================

class Bonificable:
    def __init__(self):
        self.bonificaciones = []

    def agregar_bonificacion(self, monto):
        self.bonificaciones.append(monto)

    def obtener_bonificaciones(self):
        return sum(self.bonificaciones)


# ================================
# HERENCIA MÚLTIPLE
# ================================

class EmpleadoTiempoCompletoBonificado(EmpleadoTiempoCompleto, Bonificable):
    def __init__(self, nombre, identificacion, salario_base, bonificacion):
        EmpleadoTiempoCompleto.__init__(self, nombre, identificacion, salario_base, bonificacion)
        Bonificable.__init__(self)

    def calcular_salario(self):
       
        return super().calcular_salario() + self.obtener_bonificaciones()

   
    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        info = f"Nombre: {self.nombre} | ID: {self.identificacion}"

        if mostrar_salario:
            info += f" | Salario total: {self.calcular_salario()}"

        if mostrar_detalles:
            info += f" | Bonificaciones extra: {self.obtener_bonificaciones()} | Tipo: Tiempo completo bonificado"

        print(info)


# ================================
# SISTEMA DE NÓMINA (POLIMORFISMO)
# ================================

class SistemaNomina:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def calcular_nomina(self):
        total = 0
        print("===== NÓMINA MENSUAL =====")

        for empleado in self.empleados:
            salario = empleado.calcular_salario()  
            print(f"{empleado.nombre}: {salario}")
            total += salario

        print(f"TOTAL NÓMINA: {total}")


# ================================
# PRUEBA DEL SISTEMA
# ================================

if __name__ == "__main__":

    emp1 = EmpleadoTiempoCompleto("Andres", "101", 2000, 500)
    emp2 = EmpleadoPorHoras("Laura", "102", 160, 10)
    emp3 = EmpleadoComision("Carlos", "103", 1000, 5000, 0.10)

    emp4 = EmpleadoTiempoCompletoBonificado("Sofia", "104", 2000, 300)
    emp4.agregar_bonificacion(200)
    emp4.agregar_bonificacion(150)

    sistema = SistemaNomina()
    sistema.agregar_empleado(emp1)
    sistema.agregar_empleado(emp2)
    sistema.agregar_empleado(emp3)
    sistema.agregar_empleado(emp4)

    print("--- INFORMACIÓN ---")
    emp4.mostrar_informacion()
    emp4.mostrar_informacion(True)
    emp4.mostrar_informacion(True, True)

    # Calcular nómina
    sistema.calcular_nomina()