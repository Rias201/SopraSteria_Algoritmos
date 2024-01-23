import random

# Proceso manual de inicialización
def init_num():
    return int(input("Escriba un número: "))

# Proceso automático de inicialización utilizando la aleatoriedad
# def init_num():
#     return random.randint(0,500)

num = init_num()

while num >= 0:
    print(num)
    num -= 2