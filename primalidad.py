#Este codigo busca encontrar numeros primos
def es_primo(numero):
    contador = 0

    for i in  range(1, numero + 1):#Esta parte del codigo se encarga de buscar que los numeros entre 1 e i(numero) y usa % para verificar que entre ellos no haya mas divisiones exactas
        if i == 1 or i == numero:
            continue
        if numero % i == 0: #Si aumenta el contador, significa que el numero ya no es primo
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def main():
    numero = int(input('Escriba un numero entero: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    main()