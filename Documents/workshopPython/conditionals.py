skyrats = True
ps = True
idade = 19
thunder = False


if(skyrats):
    print("Eu faço parte da skyrats :D")
else:
    print("Eu não faço parte da Skyrats :(")

# Not é uma negação
if not skyrats:
    print("Você quer fazer parte da skyrats? ")

# and -> Satisfazer as duas condições
if skyrats and idade > 18:
    print("Você é um skyrater maior de idade :O")

# or -> Satisfazer pelo menos uma das condições
if skyrats or thunder:
    print("você faz parte de um grupo de extensão!")

# Quantas condições quiser
if(skyrats):
    print("Eu faço parte da skyrats :D")
elif ps:
    print("Nosso processo seletivo está aberto!! Venha voar com a gente")
else:
    print("Aguarde nosso processo seletivo abrir, fique por dentro!!")





