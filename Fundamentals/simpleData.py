#TIPO DE DATOS STRNGS 
#PERMITE ESCRIBIR STRINGS EN UNA SOLA LINEA
write = 'Sirve para escirbir en una sola linea'
write1 = "Sirve para una sola liena"

#PERMITE ESCRBIR STRINGS EN MULTIPLES LINEAS
write2 = """Sirve para crear varias lineas:
    Line one
    Line two
    line three
"""

write3 = '''Sirve para crear varias lineas:
    lINE ONE
    LINE TWO
    LINE THREE
'''

#TIPO DE DATOS NUMERICOS Y FLOTANTES 
number = 2023 #Int
numberfloat = 12.6 #Flotantes se manejan por puntos 

#Tipos de datos booleanos 
boolean = True #La primera letra se debe colocar en mayuscula
boolean2 = False #La primera letra se debe colocar en mayuscula

#Las variables se pueden reedefinir
name = 'Jesus'
name = 'Rosml'
name = 'Hidalgo'

print(name)

#Concatenacion de strings

concatenar = 'Jesus'
concatenar2 = 5
#Concatenar con f-strings
union = f"{concatenar} te ganaste {concatenar2} canicas"
union = f"coca" + "10" #Todo lo convierte a texto.

print(union)

python = 'Me eliminaron pa'

print(python)
del python #Elimina la variable

busqueda = 'Me encanta JavaScript'
#Operadores de pertenencia
print("encanta" in busqueda) #True
print("Python" not in busqueda) #True

#Camelcase
varibleNueva = True
#Snake_Case se coloca el nombre en minuscula todo
variable_nueva = False

"""
Fundición
Si desea especificar el tipo de datos de una variable, puede hacerlo con la conversión.
"""

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Desempaquetar una coleccion 
lenguage = ['Python', 'JavaScript', 'Java']
m, a, q = lenguage

print(m)
print(a)
print(q)