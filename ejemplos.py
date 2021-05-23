# -----------------------
# Cambiar tipo de dato
# -----------------------
n = 5
print(type(n))
n_string = str(n)
print(type(n_string))
print(float(n))

# -------------------------------------
# Operadores lógicos y de comparasión
# -------------------------------------
studies = True
works = False

print(studies and works)
print(studies or works)
print(not studies)
print(not works)

n1 = 5
n2 = 5
n3 = 7

print(n1 == n2)
print(n1 == n3)
print(n1 != n2)
print(n1 != n3)

print(n1 < n2)
print(n1 <= n2)

# ---------------------------
# Funciones y condicionales
# ---------------------------
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def half(n):
    if par(n):
        result = int(n / 2)
        return result
    elif n == 11:
        return 'Ok'
    else:
        return "It's not a pair number"

print(half(10))
print(half(13))

# ----------
# Ciclos
# ----------
def loop(n):
    for i in range(1, n + 1):
        print(i)

def times_two(l):
    l_times_two = []
    for i in l:
        if i % 2 == 0:
            l_times_two.append(i)
    return l_times_two

def loop2(n):
    n2 = 0
    while n2 < n:
        print(n2 + 1)
        n2 += 1

l = [1, 4, 6, 3, 7, 39, 16, 4, 2]

loop(20)
print(times_two(l))
loop2(20)

# --------------
# Diccionarios
# --------------
my_dictionary = {
    'llave1': 1,
    'llave2': 2,
    'llave3': 3,
}
print(my_dictionary)
print(my_dictionary['llave2'])

country_poblation = {
    'Argentina': 44938712,
    'Brasil': 210147125,
    'Colombia': 50372424,
}

print(f"La población de brasil es de {country_poblation['Brasil']} habitantes")

for country in country_poblation.keys():
    print(country)

for poblation in country_poblation.values():
    print(poblation)

for country, poblation in country_poblation.items():
    print(f"La población de {country} es de {poblation} habitantes")

# ------------------------
# función con condiciones
# ------------------------
def ejemplo():
    n = input('Que quieres hacer? ')

    if n == 'suma':
        return print('suma')

    if n == 'resta':
        return print('resta')

    print('escoge entre suma o resta')

ejemplo()