import time 
start_time = time.time()

for i in range(5):
    print('Looping...', i)
    

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for idx, item in enumerate(favorites):
    print(idx, item)


lenguage = ['Java', 'Python', 'JavaScript', 'TypeScript', 'React']

for item in lenguage:
    if item == 'React':
        print(item, 'Se encontro en la lista')
        break #Rompe el bucle 
else:
    print('No se encontro en la lista')
    

numbers = 2, 1, 3, 5, 6

for item in numbers:
    if item == 3:
        continue #Salta una seccion del bucle, para luego continuar con el bucle
    print('Me gustan los numeros: ', item)       
    

#Starter Code
años = [2000, 2001, 2003, 2004, 2005]

for dessert in años:
    if dessert == 2001:
        #permite pasar por el bucle en su totalidad e ignorar eficazmente que se ha cumplido la condición 
        pass
    print('Other desserts I like are', dessert)  
    
#bucles aninados 
for x in range(10):
    print('Bucle exterior ', x)
    for y in range(10):
        print('Bucle interior ', y)
        
print(round((time.time() - start_time), 2))