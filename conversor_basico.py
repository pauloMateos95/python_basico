def conversor():
    dolares = float(input('¿Cuántos dolares tienes? '))
    valor_peso = 20

    pesos = dolares * valor_peso
    pesos = round(pesos, 2)

    print(f"Tienes ${pesos} MXN")

conversor()