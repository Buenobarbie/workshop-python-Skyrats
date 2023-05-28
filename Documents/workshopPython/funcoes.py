# Função sem argumento
def say_hello():
    print("Helloooo!!")

# Função com mais de um argumento
def check_battery(drone, bateria):
    print(f"O drone {drone} tem {bateria}% de bateria")

# Função com argumento padrão
def hello_drone(drone = "Tellinho"):
    print("Hello " + drone)

# Função com return
def square(x):
    if(type(x) == str):
        print("Não é possível efeutar a conta")
        return
    return x**2

# Função incompleta
def nada():
    pass

# Função recursiva
def rec_factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * rec_factorial(n-1)

# Funções inclusas
notas = [3.4, 5.6, 7.2, 4.6]
print(sum(notas))
print(len(notas))

soma = sum(notas)
print(round(soma))
print(max(notas))

from math import ceil, floor
print(ceil(soma))
print(floor(soma))