http_status = 550

match http_status:
    case 200 | 201: #Combinar varios literales en un solo patrón usando | («o»):
        print('Success')
    case 400:
        print('Bad Request')
    case 500 | 501:
        print('Server Error')
    case _: #El patron '_' se usa para capturar cualquier valor que no coincidan
        print('Unknown')

tuplas = (0,20)

print('#' *20)

match tuplas:
    case (0,0):
        print('Estas en el punto de origen')
    case (0,10):
        print('Has avanzado 10 kilometros')
    case (0,20):
        print('Haz llegado a la zona correcta')
    case _:
        print('No llegaste a ningun lado')