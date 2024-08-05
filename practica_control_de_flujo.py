habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python :
    print ("Cumples con los requisitos para postularte")
elif habla_ingles == False and sabe_python == False :
    print ("Para postularte, necesitas saber programar en python y tener conocimientos en ingles")
elif habla_ingles == False and sabe_python == True :
    print("Para postularte, necesitas tener conocimientos en ingles")
elif habla_ingles == True and sabe_python == False :
    print("Para postularte, necesitas saber programar en python")