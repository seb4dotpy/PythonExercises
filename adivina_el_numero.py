import random


def main():
    numero_aleatorio = random.randint(1, 100) #El pc elige de frorma aleatoria un numero entre el 1 y el 100
    numero_elegido = int(input('Elige un numero: '))
    puntaje = 100

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio: #compara el numero elegido por la pc y por el usuario, y calcula el puntaje
            print('Elige un numero mas grande. ')
            puntaje -= 1
        else:
            print('Elige un numero mas chico. ')
            puntaje -= 1
        numero_elegido = int(input('Elige otro numero: '))

    print('GANASTE!, obtuviste ' + str(puntaje) + ' puntos :D')


if __name__ == '__main__':
    main()