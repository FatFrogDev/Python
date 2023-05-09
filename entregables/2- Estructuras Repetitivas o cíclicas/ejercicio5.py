#Un grupo de 100 estudiantes presentan un examen de Física. Diseñe un diagrama que lea
# por cada estudiante la calificación obtenida y calcule e imprima:
# La cantidad de estudiantes que obtuvieron una calificación menor a 50 en el área
# del Tecnólogo en Análisis y Desarrollo de Sistemas de Información.
# La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
# La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.
# La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
estudiantes=5
nota=0
cant_menor50=0
cant_menor70=0
cant_menor80=0
cant_mayor80=0
i=1
while i<estudiantes:
    nota=float(input(f'Ingresa la nota {i} para el estudiante {i}\n'))
    if nota<0 or nota>100:
        print('Digita valores entre 0 y 100')
        print('----------------------------')
        i=estudiantes+1
    else:
        if nota<50:
            cant_menor50+=1
            i+=1
        if nota>50 and nota<70:
            cant_menor70+=1
            i+=1
        if nota >70 and nota<80:
            cant_menor80+=1
            i+=1
        if nota>80:
            cant_mayor80+=1
            i+=1
        nota=0
print(f'La cantidad de estudiantes con nota menor a 50 es de: {cant_menor50}')
print(f'La cantidad de estudiantes con nota 50 o más pero menor que 70 es de: {cant_menor70}')
print(f'La cantidad de estudiantes con nota 70 o más pero menor que 80 es de: {cant_menor80}')
print(f'La cantidad de estudiantes con nota mayor a 80 es de: {cant_mayor80}')