#Quero saber se a pessoa é Idosa, Adulta, Adolescente, Criança ou Bebê

idade = int(input("Digite a sua idade: "))

if idade >= 65:
    print("Você é Idoso")
elif idade >=18:
    print("Você é Adulto")
elif idade >=12:
    print("Você é Adolescente")
elif idade >= 3:
    print("Você é uma Criança")
else:
    print("Você é um Bebê")