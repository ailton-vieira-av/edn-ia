#Registrar as Notas dos Alunos

notas = []
numero_de_alunos = 0

while True:
    entrada = input("Digite a Nota do Aluno (ou escreva 'fim' para encerrar): ")

    #Verifica se o Professor quer encerrar
    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)

        if 0 <= nota <=10:
            notas.append(nota)
            numero_de_alunos += 1
        else:
            print("Nota inválida, Digite um valor de 0 a 10!")
    
    except ValueError:
        print("Entrada infálida. Por favor, escreva um número de 0 a 10 ou 'fim'.")

#Calcula e exibe a média

if numero_de_alunos > 0:
    media = sum(notas) / numero_de_alunos
    print(f"A média da Turma é: {media:.2f}")
    print(f"Total de Alunos computados: {numero_de_alunos}")
else:
    print("Nenhuma Nota foi registrada.")