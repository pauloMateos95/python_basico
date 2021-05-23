def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_al_reves = palabra[::-1]
    if palabra_al_reves == palabra:
        return True 
    else:
        return False


def main():
    palabra = input('Ingrese un texto: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    main()