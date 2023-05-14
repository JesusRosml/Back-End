#cadena multilinea 
x = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
"""

x = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
'''
##############################################################################################

#Python no tiene un tipo de datos de caracteres, un solo carácter es simplemente una cadena 
# con una longitud de 1.

#Acceder a elementos de la cadena 
a = "Hello, World!"
print(a[1]) #Empieza desde la posición 0

#Recorrer los caracteres de una cadena
#x actua como una variable y por cada bucle se le asigna una letra
for x in "banana":
  print(x) #Repasa las letras de la palabra "banana"

#Longitud de la cadena 
a = "Jesus Rosml"
print(len(a))

##############################################################################################

#Comprobar cadena
name = "Fernando Herrera es Full-Stack"
print("0" in name) #verificar si una determinada frase o carácter está presente en una cadena

if "Full-Stack" in name:
    print("Es un excelente desarrollador")

if "Front-End" not in name:
    print("Tienes un perfil interesante")

#verificar si una determinada frase o carácter NO está presente en una cadena    
print("Design UX" not in name) 

##############################################################################################
#Cortar cadenas

#Especifique el índice inicial y el índice final, para devolver una parte de la cadena.
b = "Hello, World!"
print(b[2:5])
#Comienza en el primer caracter y termina en el caracter numero 5
print(b[:5])
#Empieza de la cadena
print(b[2:])

#Con los indices negativos, ya no se empieza a cortar la cadena de izquierda a derecha
#Ahora se corta de derecha a izquierda 
print(b[-5:-2]) #orl

##############################################################################################

#Modificar cadenas 
upper_case = 'me han convertido a mayuscula'
print(upper_case.upper()) #Upper convierte el texto a Mayuscula

lower_case = 'ME HAN CONVERTIDO A MINUSCULAS'
print(lower_case.lower()) #Lower convirte el texto a minusculas

strip_strings = '  Soy Desarrollador Back-End  '
#Elimina espacios antes de la cadena e igual los espacios al finalizar la cadena
print(strip_strings.strip()) 

replace_strings = "Jesus Rosml es Front-End"
#remplaza una cadena con otra cadena
print(replace_strings.replace("Front-End", "Back-End")) 

split_strings = 'Jesus Rosml, Lucas Dalto, Fernando Herrara'
# convierte una cadena en una lista de elementos utilizando la coma como separador
print(split_strings.split(",")) #cada item separado por una coma es un item de lista

##############################################################################################

#Formato de cadenas 
age = 21
city = 'Coatzacoalcos'
txt = 'Mi nombres es Jesus Rosml y tengo {} años'
print(txt.format(age)) #Hace posible el insertar numeros en cadenas
#Es una versión mas reciente para combinar cadenas con datos numericos
print(f"Hola, me llamo Jesus Rosml, soy de {city} y tengo {age} años")

#Puede usar números de índice {0}para asegurarse de que los argumentos se colocan en los 
# marcadores de posición correctos:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Caracteres de escape
#Este signo \ permite colocar caracteres que no son validos en una cadena
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

strings = "Hola me llamo Jesus Rosml \
y me gusta programar \
en Python"

strings_one = 'Comenzando a programar' \
    ' Con python'
        
print(strings_one)