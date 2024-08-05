#Reutilizar codigo
#tipos: for: N veces (limite) - while : infinito
# nombres = ['juan', 'ana', 'carlos', 'Jhon', 'Sebastian']
# for elemento in nombres:
#     print("mmm" + elemento)
#---- for item in iterable :
        #expresion
#-------
# lista = ['a', 'b','c']

# for letra in lista: #Despues de : existe el cuerpo de for
#         print("letra: " + letra) 
        
# for letra in lista:
#         numero_letra = lista.index(letra) + 1 #Inicie item desde 1
#         print(f"Letra {numero_letra}: {letra}")

# lista2 = ['Jhon', 'Laura', 'Jhoana', 'Alexander', 'Luis']
# for nombre in lista2:
#         if nombre.startswith('J'): #starwith: Si el nombre comienza con J lo muestra:
#                 print(nombre)
#         else:
#                 print("El nombre no coincide con l")
        
# palabra = "Python es genial"
# for letra in palabra:
#         print(letra) #Muestra elementos de la cadena
        
# for letra in 'Python':
#         print(letra)
        
# for numero in (1,2,3,4):
#         print(numero)
        
# for numero in [(1,2), (3,4), (5,6)]:
#         print(numero)
        
# for a,b in [(1,2), (3,4), (5,6)]:
#         print(a) #muestra primera posicion de lista
        
# dic = {'clave1':'a', 'clave2':'b', 'clave3':'c'}
# for item in dic:
#         print(item)
        
# for item in dic.items():
#         print(item)
        
# for item in dic.values(): #muestra las claves
#         print(item)

alumno_clase = ['Jhon', 'Jhoana', 'Alexander', 'Valentina', 'Danyely', 'Paola', 'Andres']
for nombre in alumno_clase:
        print("Hola "+ nombre)