VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
TURQUEZA = '\033[36m'
CINZA = '\033[37m'
RESET = '\033[0m'


pessoas = []

while True:
    print('=' * 30)
    print(VERDE +'     SISTEMA DE CADASTRO' + RESET)
    print('=' * 30)
    print('''    [ 1 ] Cadastrar usuários
    [ 2 ] Listar usuários
    [ 3 ] Excluir usuário
    [ 4 ] Sair 
    ''' + RESET)
    print('=' * 30)

    opcao = int(input(TURQUEZA + 'Escolha uma opção: ' + RESET))

    if opcao == 1:
        print(VERDE +'CADASTRAR USUÁRIO' + RESET)
        print('=' * 30)

        nome = input(TURQUEZA + 'Nome: ' + RESET)
        idade = int(input(TURQUEZA +'Idade: ' + RESET))
        email = input(TURQUEZA +'Email: ' + RESET)

        print(VERDE +'USUÁRIO CADASTRADO COM SUCESSO!' + RESET)

        pessoa =[nome, idade, email]
        pessoas.append(pessoa)

    elif opcao == 2:
        print(MAGENTA +'PESSOAS CADASTRADAS' + RESET)

        if len(pessoas) == 0:
            print(MAGENTA +'Nenhuma pessoa cadastrada' + RESET)
        else:
            for i, p in enumerate(pessoas):
                print(MAGENTA +f'{i} - Nome: {p[0]} | Idade: {p[1]} | Email: {p[2]}' + RESET)


    elif opcao == 3:
        print(AMARELO +'EXCLUIR USUÁRIO' + RESET)

        if len(pessoas) == 0:
            print(VERMELHO +'Nenhuma pessoa para excluir' + RESET )

        else:
            for i, p in enumerate(pessoas):
                print(f'{i} - {p[0]}')

            indice = int(input(TURQUEZA +'Digite o número de usuário que deseja excluir: ' + RESET))

            if 0 <= indice < len(pessoas):
                pessoas.pop(indice)
                print(VERDE +'Usuário excluido com sucesso' + RESET)
            else:
                print(VERMELHO +'Número inválido! Digite novamente' + RESET)

    elif opcao == 4:
        print(VERDE +'PROGRAMA ENCERRADO! Volte sempre!' + RESET)
        break

    else:
        print(VERMELHO +'Opção inválida! Tente novamente' + RESET)