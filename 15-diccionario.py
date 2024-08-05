#consta de nombre de la variable, elementos: item :claves y item: valor
#Se puede acceder mendiante la clave
# mi_dic = { 'c1':'valor1',  'c2':'valor2'}
# print(type(mi_dic))

# resultado = mi_dic['c1']
# print(resultado)

# cliente = {'nombre':'Jhon', 'apellido':'Romero', 'peso':90, 'talla':1.82}


# consulta = cliente['nombre']
# print(consulta)
# consulta = cliente['talla']
# print(consulta)

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200} }
#acceder al elemento mediante su posicionamiento
print(dic['c2'][1]) #Acceder a la clave[c2], el valor [1]
print(dic['c3']['s2'])

dic2 = {'c1':['a','b','c'], 'c2':['d','e',]}

print(dic2['c2'][1].upper())

dic3 = {1:'a', 2:'b222222222222222222222222'}
dic3[3]='c'
print(dic3)