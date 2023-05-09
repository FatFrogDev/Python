#En una tienda de descuento las personas que van a pagar el importe de su compra llegan a
#la caja y sacan una bolita de color, que les dirá que descuento tendrán sobre el total de su
#compra. Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta
#que cierra.
# Se sabe que, si el color de la bolita es rojo, el cliente obtendrá un 40% de
#descuento; si es amarilla un 25% y si es blanca no obtendrá descuento
continuar = 1
while continuar==1:
    compra=float(input('Ingresa el valor base de la compra y saca la bolita de color\n'))
    color=input('¿De qué color es la bolita? \n')
    descuento=0
    if color=='roja':
        descuento=0.4
    elif  color=='amarilla':
        descuento=0.25
    elif color=='blanca':
        descuento=0
    else:
        print('Solo puedes elegir entre "roja" o "amarilla"')
        descuento=0
    # Imprimimos el total de la compra con o sin descuento.
    print(f'El valor total de la compra es de: {compra-(compra*descuento)}')
    # Reestablecemos valores para no acumularlos en el ciclo.
    compra=0
    descuento=0
    continuar= int(input('¿Deseas registrar otra compra? Responde 1.(si) 2.(no)\n'))
    # Operador ternario que controla el ciclo while.
    continuar = 1 if continuar==1 else 2