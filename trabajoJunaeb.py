'''
Después de la Pandemia, la cafetería de la Junaeb quiere implementar una aplicación nutricional para los alumnos que la usan para sus colaciones. 
En general, la Junaeb aconseja un máximo de 3 alimentos que pueden ser altos en calorías, grasas o carbohidratos, 
sin embargo, existe un tope máximo diario de estas últimas unidades que son las más importantes de medir. 
Si el alumno supera el máximo de 12 gramos de grasas, a mediano plazo aumentaría el riesgo cardiovascular. 
Si supera el máximo de 300 carbohidratos, tiene riesgo de no quemar esa energía con la actividad diaria y por consecuencia almacenarla como grasa en el cuerpo. 
Finalmente, si supera las 1000 calorías diarias, se proyecta que aumentaría desde 2 kilos o más a finalizar el año.

La Junaeb necesita que le ayuden a modelar un programa en Python que le permita al alumno consultar un conjunto de alimentos y le entregue el total de calorías,
grasas y carbohidratos consumidos, para finalmente informarle si sobrepasa el tope máximo diario de cada componente. Analice el siguiente ejemplo:
Si el alumno consulta por los alimentos CocaZero, McDonald y Torta, el programa debería informarle lo siguiente:
Calorías= 674, grasas= 26,6, carbohidratos = 118, Atención!: Supera las grasas y los carbohidratos
Diseñe el programa tomando como ejemplo las tablas anteriormente mostradas y desarrolle las rutinas de consulta de alimentos ingresadas por el alumno para luego entregarles la salida correspondiente. Documente en el programa, cómo resolvió el proceso de búsqueda y cálculo de cada alimento, además del el resultado que entrega. 


'''
def main():

    #Defino los valores nutricionales de cada producto en un diccionario
    cocaZero = {   
        'calorias' : 0, 'grasas' : 0, 'carbohidratos' : 0
    }

    mcDonalds = {
        'calorias' : 312, 'grasas' : 11, 'carbohidratos' : 40
    }

    pan = {
        'calorias' : 145, 'grasas' : 0.4, 'carbohidratos' : 27.5
    }

    torta = {
        'calorias' : 362, 'grasas' : 10, 'carbohidratos' : 63
    }

    pizza = {
        'calorias' : 580, 'grasas' : 15.6, 'carbohidratos' : 78
    }

    productos = int(input('Cuantos productos desea llevar?')) #Le pregunto al usuario cuantos productos va a ordenar
    #Si la cantidad de productos es mayor o igual al liminite especificado, se enviaran alertas
    if(productos > 3):
        print('ALERTA! La junaeb aconseja que lleves un maximo de 3 alimentos, por tu propia salud')
    elif(productos == 3):
        print('ALERTA! La junaeb aconseja un maximo de 3 alimentos, y estas llevando el maximo, es por tu salud')

    i = 0
    sumaCalorias = 0
    sumaCarbohidratos = 0
    sumaGrasas = 0

    while (i < productos): #Bucle que permite que el programa muestre todos los productos
        codigoProducto = int(input('Que producto desea llevar?'))
        print('')
        #Muestra el valor nutricional de los distintos productos
        if codigoProducto == 1: 
            for tipoNutiricion, valorNutricion in cocaZero.items():
                print(tipoNutiricion + 'tiene ' + str(valorNutricion))
                print('')
            sumaCalorias += cocaZero['calorias']
            sumaGrasas += cocaZero['grasas']
            sumaCarbohidratos += cocaZero['carbohidratos']

        elif codigoProducto == 2:
            for tipoNutiricion, valorNutricion in mcDonalds.items():
                print(tipoNutiricion + 'tiene ' + str(valorNutricion))
                print('')
            sumaCalorias += mcDonalds['calorias']
            sumaGrasas += mcDonalds['grasas']
            sumaCarbohidratos += mcDonalds['carbohidratos']

        elif codigoProducto == 3:
            for tipoNutiricion, valorNutricion in pan.items():
                print(tipoNutiricion + 'tiene ' + str(valorNutricion))
                print('')
            sumaCalorias += pan['calorias']
            sumaGrasas += pan['grasas']
            sumaCarbohidratos += pan['carbohidratos']

        elif codigoProducto == 4:
            for tipoNutiricion, valorNutricion in torta.items():
                print(tipoNutiricion + 'tiene ' + str(valorNutricion))
                print('')
            sumaCalorias += torta['calorias']
            sumaGrasas += torta['grasas']
            sumaCarbohidratos += torta['carbohidratos']

        elif codigoProducto == 5:
            for tipoNutiricion, valorNutricion in pizza.items():
                print(tipoNutiricion + 'tiene ' + str(valorNutricion))
                print('')
            sumaCalorias += pizza['calorias']
            sumaGrasas += pizza['grasas']
            sumaCarbohidratos += pizza['carbohidratos']

        i+=1

    print('El valor de lo que consumira es', sumaCalorias, ' calorias ', sumaGrasas, ' Grasas ', sumaCarbohidratos, ' Carbohidratos') #muestra por pantalla lo que se consumira

    if sumaCalorias > 1000: #valida las cantidades, en caso de estar altas, enviara una alerta
        print('ALERTA! usted estara consumiendo un total de ', sumaCalorias, ' estan altas')
    if sumaCarbohidratos > 300:
        print('ALERTA! usted esta consumientod un total de ', sumaCarbohidratos, ' estan altos')
    if sumaGrasas > 12:
        print('ALERTA! usted esta consumiendo un total de ', sumaGrasas, ' estan altas')

if __name__=='__main__':
    main()