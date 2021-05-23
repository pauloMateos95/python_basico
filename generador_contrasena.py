import random

# random es una librería de python que se utiliza para generar un número random
# contiene varias funciones para saber de donde sacar el número random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena 


def main():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    main()