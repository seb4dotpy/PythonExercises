'''
Parte de la información que el portal académico registra cada semestre para los alumnos, es su inscripción de asignaturas.
Las asignaturas se identifican por clave, nombre, profesor, horario, así como lo muestra el siguiente ejemplo:

Alumna: Juanita Pérez.
Inscripción: 
123, Programación, Giglia Gómez, (Lu-10:15, Ma-10:15, Ma-12:00)
123, Algebra, Rodrigo Sepúlveda, (Lu-8:30, Mi-8:30, Vi-8:30)
125, Introducción, Felipe Caselli, (Ma-8:30, Ju-8:30)
126, Tipe I, Roberto Bravo, (Ju-10:15, Vi-10:15)

Últimamente, el módulo del portal que gestiona el listado de asignaturas inscritas por el alumno ha fallado y la UV necesita que los alumnos
 de programación de ICO 123 ayuden a rediseñar el módulo realizando lo siguiente:
Suponiendo que las asignaturas antes mostradas forman parte de la base de datos, desarrolle un programa en python que le permita al alumno:
1.- desinscribir una asignatura
2.- inscribir una asignatura (solo en el caso que las asignaturas inscritas sean menores a 4)
3.-Cambiarle el nombre del profesor a alguna asignatura elegida

Desarrolle el programa usando la estructura diccionario suponiendo que puede llenarse con un máximo de 4 asignaturas. 
Puede trabajar con el diccionario lleno utilizando como contenido el que se mostró como ejemplo.
Documente como realizó cada uno de los puntos 1, 2 y 3.

'''
def main():
    programacion = {
        'codigo' : 123 ,'nombre' : 'Programacion', 'profesor' : 'Giglia Gomez', 'horario' : '(Lu-10:50, Ma-10:15, Mi-12:00)'
    }
    algebra = {
        'codigo' : 124 ,'nombre' : 'Algebra', 'profesor' : 'Rodrigo Sepulveda', 'horario' : '(Lu-08:30, Mi-08:30, Vi-08:30)'
    }
    introduccion = {
        'codigo' : 125 ,'nombre' : 'Introduccion', 'profesor' : 'Felipe Castelli', 'horario' : '(Ma-08:30, JU-08:00)'
    }
    tipe_i = {
        'codigo' : 126 ,'nombre' : 'Tipe I', 'profesor' : 'Roberto Bravo', 'horario' : '(Ju-10:15, Vi-10:15)'
    }

    asignaturasAlumno = []

    tablaAsignaturas = '''
    ############################################################
    #                                                          #
    # programacion - codigo 123 - Lu-10:50, Ma-10:15, Mi-12:00 #
    # algebra - codigo 124 - Lu-08:30, Mi-08:30, Vi-08:30      #
    # introduccion - codigo 125 - Ma-08:30, JU-08:00           #
    # tipe i - codigo 126 - Ju-10:15, Vi-10:15                 #
    #                                                          #
    ############################################################
    '''
    
    #Inscribe asignaturas
    imptabla = input('Si no conoces los datos necesarios, puedes escribir "tabla", si no presiona enter')
    if imptabla == 'tabla':
        print(tablaAsignaturas)
    else:
        pass

    if len(asignaturasAlumno) < 4:
        solicitarCodigo = (input('ingrese codigo o nombre de la asignatura que desea agregar: '))
        if solicitarCodigo == 123 or solicitarCodigo == 'programacion':
            asignaturasAlumno.append(programacion.values())
        elif solicitarCodigo == 124 or solicitarCodigo == 'algebra':
            asignaturasAlumno.append(introduccion.values())
        elif solicitarCodigo == 125 or solicitarCodigo == 'introduccion':
            asignaturasAlumno.append(introduccion.values())
        else:
            asignaturasAlumno.append(introduccion.values())

    #Desinscribe asignatura
    eliminarAsignatura = input('Deseas eliminar alguna asignatura?')
    if eliminarAsignatura == 'si':
        solicitarCodigo = (input('Ingrese el codigo o nombre de la asignatura que desea eliminar: '))
        if solicitarCodigo == 123 or solicitarCodigo == 'programacion':
            asignaturasAlumno.pop(programacion.values())
        elif solicitarCodigo == 124 or solicitarCodigo == 'algebra':
            asignaturasAlumno.pop(introduccion.values())
        elif solicitarCodigo == 125 or solicitarCodigo == 'introduccion':
            asignaturasAlumno.pop(introduccion.values())
        else:
            asignaturasAlumno.pop(introduccion.values())

    #Cambia nombre de profesor
    cambiaNombre = (input('Desea cambiar el nombre el profesor?'))
    if cambiaNombre == 'si':
        solicitarCodigo = (input('ingrese codigo o nombre de la asignatura que desea cambiar de profesor: '))
        if solicitarCodigo == 123 or solicitarCodigo == 'programacion':
            for llave, valor in programacion.items():
                if llave == 'profesor':
                    programacion[llave] = input

        elif solicitarCodigo == 124 or solicitarCodigo == 'algebra':
             for llave, valor in algebra.items():
                if llave == 'profesor':
                    algebra[llave] = input
        elif solicitarCodigo == 125 or solicitarCodigo == 'introduccion':
             for llave, valor in introduccion.items():
                if llave == 'profesor':
                    introduccion[llave] = input
        else:
             for llave, valor in tipe_i.items():
                if llave == 'profesor':
                    tipe_i[llave] = input
   

if __name__ == "__main__":
    main()