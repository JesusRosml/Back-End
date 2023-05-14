def sum():
    print('Soy una funcion sin parametros')
    
sum()

#Funcion con parametros
def calculator(a, b):
    return a + b

print('Ingrese los datos que gusta sumar')
x = float(input())
y = float(input())

resultado = calculator(x, y)

print('Usted brindo el numero ' + str(x) + ' y tambien nos dios el siguiente numero ' \
+ str(y))

print(resultado)