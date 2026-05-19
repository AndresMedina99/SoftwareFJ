#Nombre del Estudiante: Andres Ferney Medina Ruiz
#Grupo: 213022_230
#Programa: Ingenieria Multimedia
#Codigo Fuente: Autoria Propia

#Evaluación Final POA

def calcular_bono(salario_anual, desempeno):
    if desempeno == 5:
        return salario_anual * 0.20
    elif desempeno == 4:
        return salario_anual * 0.15
    elif desempeno == 3:
        return salario_anual * 0.10
    elif desempeno == 2:
        return salario_anual * 0.05
    else:
        return 0
    
empleados = []

num_empleados = int(input("Ingrese el número de empleados a registrar: "))

for i in range(num_empleados):
    print(f"Registro del empleado {i+1}")
    
    nombre = input("Nombre del empleado: ")
    departamento = input("Departamento: ")
    salario_mensual = float(input("Salario mensual: "))
    desempeno = int(input("Nivel de desempeño (1 a 5): "))
    
    salario_anual = salario_mensual * 12
    bono = calcular_bono(salario_anual, desempeno)
    salario_total = salario_anual + bono
    
    empleados.append({
        "nombre": nombre,
        "departamento": departamento,
        "salario_anual": salario_total
    })

print("Información de Empleados")
nomina_total = 0
empleado_mayor_salario = None

for emp in empleados:
    print(f"Empleado: {emp['nombre']}")
    print(f"Departamento: {emp['departamento']}")
    print(f"Salario anual total (incluyendo bono): ${emp['salario_anual']:.2f}")
    
    nomina_total += emp['salario_anual']
    
    if (empleado_mayor_salario is None or 
        emp['salario_anual'] > empleado_mayor_salario['salario_anual']):
        empleado_mayor_salario = emp

print("Resultados Finales")
print(f"Total de nómina anual de todos los empleados: ${nomina_total:.2f}")
print(f"Empleado con el salario anual más alto: {empleado_mayor_salario['nombre']} con ${empleado_mayor_salario['salario_anual']:.2f}")