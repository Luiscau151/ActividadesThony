#Calcular cuanto tiene q pagar segun la edad
#b18=1000
#b13=800
#b5=500
Edad=int (input('porfavor ingrese la edad del consumidor'))
if Edad>18:
    Precio_Entrada=1000
    print('El Precio q tiene q pagar es ',Precio_Entrada)
elif Edad>13 and Edad <=18:
    Precio_Entrada=800
    print('El Precio q tiene q pagar es ',Precio_Entrada)
elif Edad>5 and Edad <=13:
    Precio_Entrada=500
    print('El Precio q tiene q pagar es ',Precio_Entrada)
elif Edad<=5:
    print('No Paga Entrada')


