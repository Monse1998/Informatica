# Balanceo del cilindro
from vpython import *
import math
titulo = canvas (title="Balanceo del cilindro")

# Crear el cilindro
cilindro = cylinder(pos=vector(0,-3,0), axis=vector(0,6,0), radius=1, color=color.cyan)
cilindro2 = cylinder(pos=vector(4,-3,0), axis=vector(0,6,0), radius=1, color=color.blue)

# Valores del balanceo
amplitud = 45 		# Angulo máximo de inclinación
amplitud2 = -45
frecuencia = 0.2
frecuencia2 = 0.2	# Control de la velocidad del balance
tiempo = 0
tiempo2 = 0

# Balanceo
while True:
    rate (30)
    # El movimiento será sobre X (balanceo hacia atras y delante)
    angulo = amplitud * math.sin(frecuencia * tiempo)
    cilindro.axis = vector(0,6,0)		#Aseguramos la posición en Y
    cilindro.rotate(angle=math.radians(angulo),axis=vector(1,0,0), origin=cilindro.pos)
    tiempo += 0.1
    angulo2 = amplitud2 * math.sin(frecuencia2 * tiempo2)
    cilindro2.axis = vector(0,6,0)		#Aseguramos la posición en Y
    cilindro2.rotate(angle=math.radians(angulo2),axis=vector(1,0,0), origin=cilindro.pos)
    tiempo2 += 0.1