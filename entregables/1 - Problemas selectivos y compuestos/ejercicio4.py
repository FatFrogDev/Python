# En un juego de preguntas a las que se responde “Si” o “No” gana quien responda
# correctamente las tres preguntas. Si se responde mal a cualquiera de ellas ya no se
# pregunta la siguiente y termina el juego. Las preguntas son:
# ¿Colon descubrió América?
# ¿La independencia de México fue en el año 1810?
# ¿The Doors fue un grupo de rock americano?
contador = 0
respuesta = str
print('Responde de manera exacta "si" o "no" a las siguientes preguntas')
respuesta = str(input('¿Colón descubrió América?\n'))
if respuesta=='si':
    respuesta = str(input('¿La independencia de México fue en el año 1810?\n'))
    if respuesta=='si':
            respuesta = str(input('¿The Doors fue un grupo de rock americano?\n'))
            if respuesta=='si':
                print('Felicidades, has ganado:D')
            else:
                    print('Respuesta incorrecta, has perdido:(')
    else:
            print('Respuesta incorrecta, has perdido:(')
else:
    print('Respuesta incorrecta, has perdido:(')