texto = input('Ingrese un texto de su preferencia: ')
texto = texto.lower()
#letra = input('Escoge una letra : ')
#lista para ingresar elementos desde termin
letras = []

letras.append(input('Ingrese la primera letra: '.lower()))
letras.append(input('Ingrese la segunda letra: '.lower()))
letras.append(input('Ingrese la tercera letra: '.lower()))

print("\n")
print("Cantidad de Letras :")

cantidad_letra1 = texto.count(letras[0])
cantidad_letra2 = texto.count(letras[1])
cantidad_letra3 = texto.count(letras[2])
#cadena literal
print(f"Hemos encontrado la letra {letras[0]} repetida : {cantidad_letra1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida : {cantidad_letra2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida : {cantidad_letra3} veces")


print("/n")
print("CANTIDAD DE PALABRAS")

palabra = texto.split()
print(f"Hemos encontrado {len(palabra)} palabras en tu texto.")

print("/n")
print("LETRA DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_fin}")

print("/n")
print("TEXTO INVERTIDO")
palabra.reverse()
texto_invertido = ' '.join(palabra)

print(f"Si ordenamos tu texto al reves va a decir: {texto_invertido}")


print("/n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic={True:"si", False:"no"}
print(f"La palabra python {dic[buscar_python]} se encuentra en el texto")