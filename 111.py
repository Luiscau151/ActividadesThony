candidat_a= int(input('porfavor ingrese la cantidad de votantes para a:'))
candidat_b= int(input('porfavor ingrese la cantidad de votantes para b:'))
#procesos
cant_electores = candidat_a+ candidat_b
porc_a = (candidat_a*100)/cant_electores
porc_b = (candidat_b*100)/cant_electores
#salidas
print ('El porcentaje para el A es:',porc_a)
print ('El porcentaje para el B es:',porc_b)