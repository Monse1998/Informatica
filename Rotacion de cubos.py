# Hacer rodar el cubo
from vpython import *
titulo = canvas (title="Rodar un cubo")

# Crear el Cubo
cubo = box(pos=vector(0,0,0), size=vector(2,2,2), color=color.magenta)
cubo2 = box(pos=vector(3,3,0), size=vector(1.5,1.5,1.5), color=color.cyan)
cubo3 = box(pos=vector(-3,-3,-3), size=vector(3,3,3), color=color.blue)
cubo4 = box(pos=vector(-3,3,0), size=vector(2,2,2), color=color.red)

while True:
    rate(30)					#Velocidad de rotación
    cubo.rotate(angle=0.05, axis=vector(1,0,0))
    cubo2.rotate(angle=0.05, axis=vector(0,1,0))
    cubo3.rotate(angle=0.05, axis=vector(0,0,1))
    cubo4.rotate(angle=0.05, axis=vector(1,1,1))