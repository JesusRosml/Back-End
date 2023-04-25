#Datos compuestos
#Estos es una lista no un array, y se puede modificar
lista = ['JavaScript', 'Python', 'Java', 'TypeScript']
lista[2] = 'Django' #Agregar o cambiar nuevo item en la lista
print(lista[2])
print(lista)

#Tuplas 
#la tupla no se puede modificar, pero funciona de manera similar a una lista
tupla = ('HTML5', 'CSS', 'Bootstrap', 'JavaScript', 'TypeScript', 'React', 'Git-Hub')
#tupla[2] = 'TailwindCSS'
print(tupla[2])

#Conjunto set 
#Se puede agregar o eliminar despues de su creación
conjunto = {'Papa Frita', 'Longaniza', 'Champiñones', 'Torta'}
print(conjunto) #No podemos acceder por el indice
conjunto = {'Podemos reedifinir un conjunto set, pero no modificar un elemento de el'}
print(conjunto) #No permite repetir valores duplicados
conjunto = {'Papa Frita', 'Longaniza', 'Champiñones', 'Torta', 'Longaniza'}
print(conjunto)#Son datos desornedados

#Dicicionario
diccionario = {
    #Clave : Valor
    'Nombre' : 'Jesus Rosml',
    'Edad' : 23,
    'Carrera' : 'Ingenieria Informatica',
    'Estudiante' : True,
    'Finalizo' : False
}
#Cambiar valor del diccionario
diccionario['Nombre'] = 'Angel Ricardo'
#Se accede por el name del item
print(diccionario['Nombre'])