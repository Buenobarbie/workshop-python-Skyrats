# Criando o set com chaves
# Observe que ele elimina os objetos repetidos
cesta = {"banana", "laranja", "cereja", "banana", "laranja"}
print(cesta)
# {'cereja', 'banana', 'laranja'}

# Criando o set com o método set()
# Deve-se passar um conjunto de elementos (tupla ou lista)
cesta2 = set(["banana", "laranja", "cereja", "banana", "laranja"])
print(cesta2)
# {'cereja', 'banana', 'laranja'}