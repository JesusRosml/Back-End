#Practicando con listas
list_Lenguage = ['HTML5', 'CSS', 'Bootstrap', 'TailwindCSS', #Listas aninadas
                ['JavaScript', 'TypeScript', 'Java', 'Python', 'Ruby']]

list_Lenguage[2] = 'React'
list_Lenguage[4][4] = 'C#'

print(list_Lenguage)

print()

#Practicando con tuplas 
tuplas_Game = ('Fornite', 'Minecraft', 'Clash Royale', 'Clash of clans', 
             ('Valorant', 'Overwatch', 'Gears of wars')) #Tuplas aninadas 

print(tuplas_Game[4][2])
print()

#Practicando con conjunto set

#No es recomendable hacer conjuntos aninados, es mejor usar listas o tuplas para aninar
#No se puede crear conjuntos aninados de esta manera
# conjunto_set = {{9785, 6575, 8784, 1241}, {2341, 8439, 7210}}

#Convertir listas a conjunto set (Igual crea conjuntos inmutables)
conjunto_lista1 = [2458, 5454, 4265, 2121]
conjunto_lista2 = [2341, 1111, 2222]
conjunto_setOne = {frozenset(conjunto_lista1), frozenset(conjunto_lista2)}

print(conjunto_setOne)
print()

#Practicando con diccionarios
estudiante = {
    'Name': 'Jesus Rosml',
    'Edad': 20,
    'Grado': '8AF',
    'Carrera': 'Informatica',
    'Lenguajes': {'JavaScript', 'Python'} #diccionarios aninados
}

estudiante['Edad'] = 25
print(estudiante)
print(estudiante['Edad'])
