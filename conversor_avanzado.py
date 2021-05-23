menu = """
Bienvenido al conversor de monedas

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción """

opcion = input(menu)

def conversor(tipo_peso):
    if tipo_peso == 'colombianos':
        valor_dolar = 3875
    elif tipo_peso == 'argentinos':
        valor_dolar = 65
    elif tipo_peso == 'mexicanos':
        valor_dolar = 20
    else:
        return print('Ingresa una opción valida')
    
    pesos = float(input(f"¿Cuántos pesos {tipo_peso} tienes?: "))

    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print(f"Tienes ${dolares} dolares")

if opcion == '1':
    conversor('colombianos')
elif opcion == '2':
    conversor('argentinos')
elif opcion == '3':
    conversor('mexicanos')
else:
    print('Ingrese una opción valida')