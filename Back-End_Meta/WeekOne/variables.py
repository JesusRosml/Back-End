#Una variable se crea en el momento en que le asigna un valor por primera vez.
x = 10

#Fundición
#Si desea especificar el tipo de datos de una variable, puede hacerlo con la conversión.

one = str(3) # pasa de 3 a '3'
two = int(4) # Sigue siendo 4
three = float(4) # Pasa de 4 a 4.0

#Obtener el tipo de datos de una variable 
cars = 'Automovil'
print(type(cars))

#Python distingue entre minusculas y mayusculas 
a = 2 #Son variables distintas
A = 2 #A es totalmente diferente a la variable a

#nombre de variables largas 
laptop_color_azul = 12 #Snake_Case se coloca el nombre en minuscula todo

#Asignacion del mismo valor
x = y = z = 'Orange' #asignar el mismo valor a múltiples variables en una línea

#Asigancion multiple
#Es importante asiganar los valores en el orden en que fueron declaradas las variables
d,f,g = 4,5,6

print(d)
print(f)
print(g)

#Desempaquetar una colección
#Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer 
#los valores en variables. Esto se llama desempacar .
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#variables globales 
#Las variables que se crean fuera de una función se conocen como variables globales.
variable_global = 'Soy Jesus Rosml'

def test():
    global conversion_global #Global convierte una variable local a global
    conversion_global = ' y tengo 21 años'
    
    variable_local = ' Soy desarrollador Back-End' #Fuera de esta funcion no existe 
    print(variable_global + variable_local + conversion_global)

test()
print(conversion_global) #Como podemos ver si esta disponible desde fuera de la funcion

a = isinstance ("aa", str)