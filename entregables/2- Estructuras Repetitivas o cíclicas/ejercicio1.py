#Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a
#la semana. Su política de pagos es que un vendedor recibe un sueldo base y un 10% extra
#por comisiones de sus ventas. El gerente de su compañía desea saber cuánto dinero
#obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas
#realizadas, y cuánto gana tomando en cuenta su sueldo base y sus comisiones.
#Establecemos la cantidad de vendedores que se necesiten.
vend = int(input('ingrese el número de vendedores con los que cuenta su negocio\n'))
compra = 0
sueldobase = 1000000
# Ciclo que controla la cantidad de vendedores.
for i in range(vend):
    print(f'para el vendedor {i+1}') 
    # Ciclo que controla 
    for j in range(3):
        compra = float(input(f'Ingresa el valor de la compra {i+1}\n')) + compra
        j+=1
    comision=float((compra-(compra*0.1)))
    print(f'El vendedor consiguió {comision}, en comisiones, y el total ganado es de     {int(sueldobase+comision)}')
    compra=0
    i+=1
    