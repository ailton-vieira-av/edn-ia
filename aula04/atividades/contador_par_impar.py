#Contar Pares e Impares

pares = 0
impares = 0

while True:
    entrada = input("Digite um Número Inteiro (ou 'fim' para Encerrar): ")

    if entrada.lower() == 'fim':
        print("Encerrado com Sucesso!")
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é Par. ")
            pares += 1
        else:
            print(f"O número {numero} é Impar.")
            impares += 1

    except ValueError:
        print("Erro: Digite apenas Números Inteiros")

print("\nResultado: ")
print(f"Números Pares: {pares}")
print(f"Números Impares: {impares}")