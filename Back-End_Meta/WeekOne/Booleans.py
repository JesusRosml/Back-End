boolean_true = True
boolean_false = False

#Evaluar valores y variables
#La bool()función te permite evaluar cualquier valor, y darte Trueo False a cambio
print(bool("Hello"))
print(bool(15))
print(bool(0)) #El numero 0 es el unico que dara False
print(bool("")) #Todos los valores vacíos daran False

#Puede crear funciones que devuelvan un valor booleano:
def myFunction() :
  return True

print(myFunction())

#Puede ejecutar código basado en la respuesta booleana de una función:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#Que se puede usar para determinar si un objeto es de cierto tipo de datos:
x = 200
print(isinstance(x, int))