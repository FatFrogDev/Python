#Calcular e imprimir la tabla de multiplicar de un número cualquiera
#imprimir el multiplicando, multiplicador y prodcto
# ciclo for 
num=int(input('Ingrese el número para sacar su tabla de multipllicar\n'))
for i in range(1,11):
    resultado=num*i
    print(f'{num}*{i} es igual a: {resultado}')
    i+=1
