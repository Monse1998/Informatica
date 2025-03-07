from vpython import *

# Crear cilindro
titulo = canvas (title="Cilindro en 3D")

# Crear el cilindro
cilindro = cylinder(pos=vector(0,-3,0), axis=vector(0,6,0), radius=1, color=color.cyan)

velocidad = 0.05 				#Velocidad de movimiento

while True:
    rate (30)
    cilindro.pos.x += velocidad
    
#Rebote del cilindro
    if cilindro.pos.x > 3 or cilindro.pos.x < -3:
        velocidad = -velocidad	# Cambia de direccion