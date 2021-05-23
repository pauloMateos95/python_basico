import random

# random es una librería de python que se utiliza para generar un número random
# contiene varias funciones para saber de donde sacar el número random

def main():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("""
    Tienes 7 intentos
    Elige un número del 1 al 100: """))
    ganaste = False
    for i in range(1, 8):
        if numero_elegido < numero_aleatorio:
            i = str(i + 1)
            print('Busca un número más grande')
            if i == '8':
                break
            else:
                numero_elegido = int(input('intento número ' + i + ': '))
        elif numero_elegido > numero_aleatorio:
            i = str(i + 1)
            print('Busca un número más pequeño')
            if i == '8':
                break
            else:
                numero_elegido = int(input('intento número ' + i + ': '))
        else:
            ganaste = True
            break
    if ganaste:
        print('¡Ganaste!')
    else:
        print('¡Perdiste!')
    


if __name__ == '__main__':
    main()