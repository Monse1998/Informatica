# Los conjuntos, son elementos que se agrupan en forma única y desordenada

# Para crearlo set () {}
#conjunto = set ()
#print(conjunto)
'''
conjunto={1,2,3,"david","david","ofe","ofe",1,2,3,1,2,3}
print(conjunto)

# Para agregar un elemento al conjunto
conjunto.add(4)
print(conjunto)

agre=input("Dame el valor que de deseas agragar:  ")
conjunto.add(agre)
print(conjunto)

# Para eliminar un elemento en un conjunto
conjunto.discard("david")
print(conjunto)

elimi=input("Dame el valor que deseas eliminar:  ")
conjunto.discard(elimi)
print(conjunto)

# Para buscar un elemento
print("lola" in conjunto)'''

# Union de dos conjuntos (la suma de todos sus elementos"
a={1,2,3}
b={3,2,4,5}
c=a|b
print(c)

# Interseccion de elementos que están en ambos conjuntos
d=a&b
print(d)

# Diferencia entre conjuntos que A no estan en B y viceversa
e=a-b
print(e)
e=b-a
print(e)

# Diferencia simetrica: elementos están en A y B pero no estan compartidos
f=a^b
print(f)