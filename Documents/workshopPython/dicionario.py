# Criando um dicionário que armazena o par nome/telefone
tel = {"babs" : 1234, "mari" : 5678, "lena" : 9012}
print(tel["mari"]) #5678

# Criando dicionários com loops
dic = {x: x**2 for x in (2, 4, 6)}
print(dic) # {2: 4, 4: 16, 6: 36}

# Iterando entre as chaves e valores
for k, v in tel.items():
    print(k, v)
    
# babs 1234
# mari 5678
# lena 9012