# En una llantera se ha establecido una promoción de las llantas marca “Ponchadas”,
# dicha promoción consiste en lo siguiente:
# Si se compran menos de cinco llantas el precio es de $300 cada una,
# de $250 si se compran de cinco a 10 y
# de $200 si se compran más de 10.
# Obtener la cantidad de dinero que una persona tiene que pagar por cada una
# de las llantas que compra y la que tiene que pagar por el total de la compra.
cant = int(input('¿Cuántas llantas quiere comprar?\n'))
if cant<5:
    precio=300
    print('El precio unitario por llanta es de: $', precio)
    print('El total a pagar es de: ', (cant*precio))
elif cant >=5 and cant<=10:
    precio=250
    print('El precio unitario por llanta es de: $', precio)
    print('El total a pagar es de: ', (cant*precio))
elif cant>10:
    precio=200
    print('El precio unitario por llanta es de: $', precio)
    print ('El total a pagar es de: $', (cant*precio))