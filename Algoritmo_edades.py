import random

# Proceso manual de inicialización
# def init_personas():
#     personas = []
#     for i in range(50):
#         sexo = input("Escriba el sexo de la persona: ")
#         edad = input("Escriba la edad de la persona: ")
#         personas.append((sexo,edad))
#     return personas

# Proceso automático de inicialización utilizando la aleatoriedad
def init_personas():
    sexo = ["M", "F"]
    personas = []
    for i in range(50):
        personas.append((random.choice(sexo),random.randint(0,100)))
    return personas

personas = init_personas()
totalMayores = 0
totalMenores = 0
hombresMayores = 0
mujeresMayores = 0
totalMujeres = 0

for i in range(len(personas)):
    if personas[i][1] >= 18:
        totalMayores += 1
        if personas[i][0] == "M":
            hombresMayores += 1
        else:
            mujeresMayores += 1
    else:
        totalMenores += 1
    
    if personas[i][0] == "F":
        totalMujeres += 1

print(f"Cantidad de personas mayores de edad: {totalMayores}")
print(f"Cantidad de personas menores de edad: {totalMenores}")
print(f"Cantidad de hombres mayores de edad: {hombresMayores}")
print(f"Cantidad de mujeres mayores de edad: {mujeresMayores}")
print(f"Porcentaje de personas mayores de edad respecto al total: {totalMayores/50*100}%")
print(f"Porcentaje de mujeres respecto al total: {totalMujeres/50*100}%")

print(personas)