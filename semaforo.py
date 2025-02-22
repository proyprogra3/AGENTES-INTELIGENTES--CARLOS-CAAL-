import time
import random

def semaforo():
    estados = ["verde", "amarillo", "rojo"]
    
    while True:
        vehiculos = random.randint(0, 10)  # Simulación de tráfico
        
        # Ajuste del tiempo del semáforo según la cantidad de vehículos
        tiempo_verde = 5 if vehiculos > 5 else 10
        
        for estado in estados:
            print(f"Semáforo en {estado.upper()} ({'⏳' if estado == 'amarillo' else '🚦'})")
            time.sleep(tiempo_verde if estado == "verde" else 3)

semaforo()

# Segundo commit
