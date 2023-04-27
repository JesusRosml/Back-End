ingreso_mensual = 18000
gastos_mensuales = 14000

if ingreso_mensual >= 20000:
    if gastos_mensuales < 15000: #If aninados
        print('Vivis muy bien, ademas de que administras tu dinero')
    else:
        print('Necesitas administrar mejor tu dinero')
elif ingreso_mensual >= 10000:
    print('Vivis bien')
else:
    print('Necesitas estudiar un lenguaje de programación')
    