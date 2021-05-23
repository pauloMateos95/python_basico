import random

# random es una librería de python que se utiliza para generar un número random
# contiene varias funciones para saber de donde sacar el número random

def main():
    random_number = random.randint(1, 100)
    chosen_number = int(input('Elige un número del 1 al 100: '))
    while chosen_number != random_number:
        if chosen_number < random_number:
            print('Busca un número más grande')
            chosen_number = int(input('Elige otro número: '))
        else:
            print('Busca un número más pequeño')
            chosen_number = int(input('Elige otro número: '))
    print('¡Ganaste!')

if __name__ == '__main__':
    main()