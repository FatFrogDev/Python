#El profesor de una materia desea conocer la cantidad de sus alumnos que no tienen
#derecho al examen de nivelación.
#Diseñe un algoritmo que lea las calificaciones obtenidas en las 5 materias por cada uno de
#los 40 alumnos y escriba la cantidad de ellos que no tienen derecho al examen de nivelación.
materias=5
alumnos=40
for i in range (materias):
    print(f'Para la materia {i+1} \n')
    reprobados=0
    cant_notas=int(input('¿Cuántas notas tiene esta asignatura? \n'))
    for j in range (alumnos):
        nota=0
        for k in range (cant_notas):
            nota=nota+float(input(f'Ingresa la nota {k+1} para el alumno {j+1}\n'))
        promedio=nota/cant_notas
        print(f'El promedio del alumno fue de: {promedio}')
        if(promedio<3):
            reprobados=reprobados+1
    print(f'Los alumnos sin derecho a examen de recuperación en la materia ({i+1}) fueron {reprobados}')