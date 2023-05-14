import random #Importa el módulo aleatorio

#Tipos de datos
x = 'Hello world' #str
x = 20 #int
x = 20.0 #float
x = 1j #complex 
x = ['Banana', 'Apple', 'Orange'] #list
x = ('Banana', 'Apple', 'Orange') #Tuple
x = range(6) #Range
x = {"name": 'Jesus Rosml', "age": '21 años'} #dict 
x = {"apple", "banana", "cherry"} #set
x = frozenset({"apple", "banana", "cherry"}) #frozenset
x = True #Bool
x = b"Hello" #Bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5)) #memoryview
x = None #NoneType

#Configuración del tipo de datos específico
a = str("Hello World") #str 
a = int(20) #int
a = float(20.0) #float
a = complex(1j) #complex
a = list(("Apple", "Banana", "Orange")) #List
a = tuple(("Apple", "Banana", "Orange")) #Tuple
a = range(6) #Range
a = dict(name = "Jesus", age = 20) #Dict
a = set(("apple", "banana", "cherry")) #Set
a = frozenset(("apple", "banana", "cherry")) #Frozenset
a = bool(5) #Bool
a = bytes(5) #Bytes
a = bytearray(5) #Bytearray
a = memoryview(bytes(5)) #Memoryview

#Numeros en python
#Hay tres tipos de numeros: int | float | complex 
x = 1 #Int 
y = 2.8 #Float
#También puede ser un número científico con una "e" para indicar la potencia de 10.
f = -87.7e100 #Float
#Los números complejos se escriben con una "j" como parte imaginaria
z = 1j #Complex = Complejos

#Numeros aleatorios en python
print(random.randrange(1, 10))