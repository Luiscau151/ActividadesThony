print('adivina mi color favorito')
print('----')
a=('azul')
print('ayudaditas')
print('comienza con la letra:',a[0])
print('la cantidad de letras:',len(a))
print('termina con la letra:', a[3])
a_ingresado=input('¿adivinazte cual es?')
if(a_ingresado==a):
    print('Ganaste')
else:
    print('El color era',a, 'perdiste')
