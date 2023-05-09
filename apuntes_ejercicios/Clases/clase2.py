# #26/04/2023
# ## 1- Comparadores lógicos (if)
# # If 
# llueve=False
# temperetura = 12
# if llueve==True:
#     print ('Llevaré paraguas')
# else:
#     print('No está lloviendo')
# print('Ahora saldré a la calle')
# if llueve==True and temperetura<18:
#     print ('Está lloviendo')
#     print ('Llevaré abrigo')
# else:
#     print('No está lloviendo')
# print('Ahora saldré a la calle')
# # if con or
# if llueve==True or temperetura<20:
#     print ('Está lloviendo')
#     print ('Llevaré abrigo')
# else:
#     print('No está lloviendo')
# # Ejemplo de if erróneo por sintaxis
# # if llueve==True or temperetura<20:
# #     print ('Está lloviendo')
# # print ('Llevaré abrigo')
# # else:
# #     print('No está lloviendo')

# # if sin else
# charcho = True
# print('Comienzo de la caminata')
# if charcho == True:
#     print('¡A saltar!')
# print('Fin de la caminata')
# Decisiones complejas
# if con and 
# condicional elif
# if (condición)
# Instrucciones
# elif (Condición)
# instrucciones
# else
# instrucciones

#Ejercicio 1
# Un hombre desea saber cuanto dinero se genera por concepto de intereses
# sobre la cantidad que tiene en inversión en el banco.
# El decide reinvertir siempre y cuando estos excedan $7000, 
# y en ese caso dinero desea saber cuanto dinero tiene en su cuenta

# cap = float(input('Ingresa el capital \n'))
# p_int = float(input('Ingresa los intereses \n'))
# capf = int((cap*p_int)+cap)
# if capf >7000:
#     print('Su capital fianl es de:', capf, '\npuede reinvertir.')
# else:
#     print('Tiene ', capf, ' de capital, no debería reinvertir')

# Ejercicio 2
# En un almacén se hace un 20% de descuento a los clientes cuya compra
# supere los $1000. ¿Cuál será la cantidad que pagará una persona por su compra?

compra = float(input('Ingresa el valor de la compra \n'))
if compra>1000:
    total = float((compra-(compra*0.20)))
    print ('El valor total era de: ', compra, ', con su descuento queda en: ', total)
else:
    print ('El valor total es de: ', int(compra))