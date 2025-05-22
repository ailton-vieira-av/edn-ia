#Trata erro de conversão de tipo

try:
    # Código que pode gerar um erro
    numero = int(input("Digite um Número: "))
    print(f"Você digitou o Número {numero}")
except ValueError:
    # Código executado se der erro
    print("Isso não é um Número inteiro! Por favor, verifique!")