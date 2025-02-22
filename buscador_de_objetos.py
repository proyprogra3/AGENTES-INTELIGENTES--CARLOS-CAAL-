import random

# Tamaño de la cuadrícula
tamaño = 5

# Inicializar la cuadrícula con valores vacíos
cuadricula = [['.' for _ in range(tamaño)] for _ in range(tamaño)]

# Posición inicial del agente
agente_pos = [0, 0]

# Colocar el objeto aleatoriamente
objeto_pos = [random.randint(0, tamaño - 1), random.randint(0, tamaño - 1)]

# Función para mostrar la cuadrícula
def mostrar_cuadricula():
    for i in range(tamaño):
        for j in range(tamaño):
            if [i, j] == agente_pos:
                print('A', end=' ')
            elif [i, j] == objeto_pos:
                print('O', end=' ')
            else:
                print('.', end=' ')
        print()

# Función para mover el agente
def mover_agente():
    global agente_pos
    if agente_pos[0] < objeto_pos[0]:
        agente_pos[0] += 1
    elif agente_pos[0] > objeto_pos[0]:
        agente_pos[0] -= 1
    elif agente_pos[1] < objeto_pos[1]:
        agente_pos[1] += 1
    elif agente_pos[1] > objeto_pos[1]:
        agente_pos[1] -= 1

# Bucle de movimiento
while agente_pos != objeto_pos:
    mostrar_cuadricula()
    print("Movimiento del Agente...")
    mover_agente()
    input("Presiona Enter para mover al agente un paso más...")
    
mostrar_cuadricula()
print("¡Agente ha encontrado el objeto!")

