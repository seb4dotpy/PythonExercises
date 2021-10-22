import random


def generar_contrasena():
    mayusculas = ['A','B', 'C','D','E','F','G','H','I','J','K','L']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l']
    simbolos = ['!','@','#','$','%','^','&']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros #junta las 3 listas

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres) #elige un caracter aleatorio
        contrasena.append(caracter_random) #guarda el caracter en la lista

    contrasena = ''.join(contrasena) #transorma la lista a un String
    return contrasena


def main():

    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)


if __name__ == '__main__':
    main()
