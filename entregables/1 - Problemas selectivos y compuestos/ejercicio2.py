# En una fábrica de computadoras se planea ofrecer a los clientes un descuento que
# dependerá del número de computadoras que compre. Si las computadoras son menos
# de cinco se les dará un 10% de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco, pero menos de diez se le otorga un 20% de
# descuento; y si son 10 o más se les da un 40% de descuento. El precio de cada
# computadora es de $15,000
cant = int(input('¿Cuántas computadoras quiere comprar?\n'))
precio = 15000
total = cant*precio
if cant <5:
    print('El total es de: $', int((total-(total*0.1))))
elif cant >= 5 and cant<10:
    print('El total es de: $', int((total-(total*0.2))))
elif cant>=10:
    print('El total es de: $', int((total-(total*0.4))))