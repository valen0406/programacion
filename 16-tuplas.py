#Para guardar infomracion que no se va a modificar. Estructura de datos donde permite manejar diferentes tipos de datos:string,entero.. Son ordenadas, posicionamiento, duplicados
# mi_tupla = (1,2,3,4)
# print(type(mi_tupla)) #Especifica la estructura que estoy usando

# mi_tupla2 = (1,2,(10,20),4)
# print(mi_tupla2[2][1])

# #pasar tupla a una lista
# mi_tupla = list(mi_tupla) #casteo_ cambiar type()
# print(type(mi_tupla))

# t = (1,2,3)
# x,y,z = t
# print(x,y,z)

# from this import d


# print(len(t)) #especificar cuantos elementos en una tupla: len


#2:casteo
#3:
# j = (1,2,3,4)
# x,y,z = t
# print(x,y,z)

#ejercicio 1
mi_tupla = (1,2,3,2,3,1,3,2,3,3,3,1,3,2,2,1,3,2)
count = mi_tupla.count(2)
print(count)

#ejercicio 2
mi_tupla2 = (1,2,3,2,3,1,3,2)
mi_lista = list(mi_tupla2)#casteo
print(type(mi_lista))

#ejercicio3
mi_tupla3 = (1,2,3,4)
a, b, c, d = mi_tupla3
print(a, b, c, d)