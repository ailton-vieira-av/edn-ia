#Verificar se a senha é forte tendo 12 dígitos ao menos um número

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar)")

    #Verifica se o usuário deseja sair
    if senha.lower() == 'sair':
        print("Programa encerrado")
        break

    tem_numero = False

    #Verifica se tem ao menos um número

    for char in senha:
        if char.isdigit():
            tem_numero = True
            break

    #Precisa ter 12 caracteres e um número

    if len(senha) < 12:
        print("Senha fraca: Ela deve ter ao menos 12 caracteres!")
    elif not tem_numero:
        print("Senha fraca: Precisa ter ao menos um número!")
    else:
        print("Senha validada com sucesso!")
        break