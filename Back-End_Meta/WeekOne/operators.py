#Operadores aritmeticos 

#Los operadores aritméticos se utilizan con valores numéricos para realizar operaciones 
#matemáticas comunes:

print(4 + 6) #operador de adición
print(4 - 6) #Operador de Sustracción
print(4 * 6) #Operador de multiplicación 
print(4 / 6) #Operador de división 
print(4 % 6) #Operador de modulo 
print(4 ** 6) #Operador de exponenciacion
#devuelve el resultado de la división como un número entero redondeado al entero 
#más cercano hacia abajo.
print(4 // 6) #Operador Floor division	
print()
#Operadores de asignación
x = 5
x += 3
x -= 3
x *= 5
x /= 3
x %= 3
x //= 2
x **= 5

print(x)
print()

#Operadores de comparación 
u = 2 == 2
u = 2 != 2
u = 2 > 2
u = 2 < 2
u = 2 >= 2
u = 2 <= 2

#Operadores logicos 
x = 4 < 10 and 4 < 5 #devuelve True si ambas expresiones son verdaderas
x = 5 < 20 or 5 < 12 #devuelve True si al menos una de ellas es verdadera.
x = not(5 < 20 or 5 < 12) #invierte el valor de verdad de una expresión

#Operadores de identidad 
f = ['Java', 'Python']
c = ['Java', 'Python']
l = f 

print(f is l)
print(f is c)
print(f == c)
print()
print(f is not l)
print(f is not c)
print(f == c)
print()
#Operadores de membresia 
p = 'Me llamo Jesus Rosml'
print('Jesus' in p) #devuelve True si el valor o variable se encuentra en la secuencia.
print('Rosml' not in p) #devuelve True si el valor o variable no se encuentra en la secuencia.

#Operadores bit a bit 
v = 20

v &= 4
v |= 5
v ^= 3	
v >>= 3	
v <<= 3	

print(v)

#Prescedencias de operadores 

#Los paréntesis tienen la prioridad más alta, lo que significa que las expresiones entre 
# paréntesis deben evaluarse primero:

print((6 + 3) - (8 + 2)) 

print(100 + 5 * 4) #La multiplicacion se resuelve primero 