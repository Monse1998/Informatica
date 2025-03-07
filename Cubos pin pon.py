from vpython import *
titulos=canvas(title="Cubo en 3D")

#Crea un cubo
cubo=box(pos=vector(2,0,0),size=vector(2,2,2),color=color.magenta)
cubo2=box(pos=vector(5,4,0),size=vector(2,2,2),color=color.cyan)
cubo3=box(pos=vector(0,2,0),size=vector(2,2,2),color=color.white)

#Velocidades iniciales de los cubos
incremento=0.1
incremento2=0.2
incremento3=0.3

while True:
        rate(30)						#Velocidad de animación
        cubo.pos.y += incremento
    
        if cubo.pos.y > 5 or cubo.pos.y < -5:
            incremento=-incremento	#Invertir dirección
        
        cubo2.pos.y += incremento2      
        if cubo2.pos.y > 5 or cubo2.pos.y < -5:
            incremento2=-incremento2	#Invertir dirección
        
        cubo3.pos.y += incremento3
        if cubo3.pos.y > 5 or cubo3.pos.y < -5:
            incremento3=-incremento3	#Invertir dirección