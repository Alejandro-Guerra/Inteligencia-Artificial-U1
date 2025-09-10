import random
import time
import os


FILAS = 8
COLUMNAS = 8

# Símbolos
VACIO = '.'
OBSTACULO = '#'
ROBOT = 'R'

# Crea una matriz(grid)
grid = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Coloca los obstáculos aleatoriamente 
for _ in range(12):
    f = random.randint(0, FILAS-1)
    c = random.randint(0, COLUMNAS-1)
    grid[f][c] = OBSTACULO

# Pone al "robot" en un lugar aleatoreo
while True:
    f = random.randint(0, FILAS-1)
    c = random.randint(0, COLUMNAS-1)
    if grid[f][c] == VACIO:
        robot_f, robot_c = f, c
        grid[robot_f][robot_c] = ROBOT
        break

# Direcciones posibles: arriba, derecha, abajo, izquierda
direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direccion_actual = 0  # Comienza "mirando" arriba

def mostrar_grid():
    os.system('cls' if os.name == 'nt' else 'clear')  # limpia la consola
    for fila in grid:
        print(' '.join(fila))
    print("\nCtrl + C para detener.\n")

# Simulación
try:
    while True:
        mostrar_grid()
        time.sleep(0.5)

        # Quitar robot de la celda actual
        grid[robot_f][robot_c] = VACIO

        # Calcular siguiente celda
        df, dc = direcciones[direccion_actual]
        nueva_f = robot_f + df
        nueva_c = robot_c + dc

        # Reglas reactivas:
        # 1. Si la celda adelante está libre, avanzar
        if (0 <= nueva_f < FILAS and 0 <= nueva_c < COLUMNAS and grid[nueva_f][nueva_c] == VACIO):
            robot_f, robot_c = nueva_f, nueva_c
        else:
            # 2. Si no puede avanzar, girar a la derecha
            direccion_actual = (direccion_actual + 1) % 4

        # Colocar robot en la nueva celda
        grid[robot_f][robot_c] = ROBOT

except KeyboardInterrupt:
    print("\nSimulación detenida.")


