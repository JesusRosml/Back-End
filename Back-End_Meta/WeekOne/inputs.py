print('Bienvenido a la calculadora')
#Esta función se puede utilizar para convertir el valor proporcionado en un int
number_one = int(input('Ingrese el primer numero: '))
number_two = int(input('Ingrese el segundo numero: '))

print(number_one + number_two)
print('-'*10)
#Esta función se puede utilizar para convertir el valor proporcionado en una String
number_three = 20
print(str(number_three))
print('-'*10)
#Esta función se puede utilizar para convertir el valor proporcionado en un float
number_float = 80
print(float(number_float))
print('-'*10)

name_one = int(input('Ingrese un numero random: '))
name_two = int(input('Ingrese otro numero random: '))

print('Hola mi estimado {}, espero tenga un exlente dia, \
me gusto su segundo nombre {}'.format(name_one, name_two))

#especifica que se desea formatear el valor numérico como un número de punto flotante con 
# dos decimales.
print('Hola mi estimado {:.2f}, espero tenga un exlente dia, \
me gusto su segundo nombre {:.2f}'.format(name_one, name_two))