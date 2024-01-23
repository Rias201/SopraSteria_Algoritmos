import random

# Proceso manual de inicialización
def init_salario():
    tarifa = float(input("Cuál es la tarifa base del trabajador? "))
    horasTrabajadas = int(input("Cuántas horas ha trabajado el trabajador? "))
    return tarifa, horasTrabajadas

# Proceso automático de inicialización utilizando la aleatoriedad
# def init_salario():
#     tarifa = 10
#     horasTrabajadas = random.randint(20,60)
#     return tarifa, horasTrabajadas

tarifa, horasTrabajadas = init_salario()

if horasTrabajadas > 40:
    horasExtras = horasTrabajadas - 40
    precioHorasExtras = horasExtras * (tarifa*1.5)
    sueldo = 40*tarifa + precioHorasExtras
else:
    sueldo = horasTrabajadas*tarifa

print(f"El sueldo del trabajador es de {sueldo}€")