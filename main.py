
chaves = ('Nome','CPF','Telefone','E-mail','Profissão','Empresa')

pessoas = []

while True:

    print('Ações Disponiveis:')
    print('Cadastrar = 1')
    print('Leitura = 2')
    print('Alteração = 3')
    print('Deletar = 4')

    funcao = int(input('Informe o número da ação desejada: '))
        
    match funcao:
        
            case 1:
                pessoa = { 
                chaves[0]:input('Informe o Nome: '),
                chaves[1]:input('Informe o CPF: '),
                chaves[2]:input('Informe o Telefone: '),
                chaves[3]:input('Informe o E-mail: '),
                chaves[4]:input('Informe a Profissão: '),
                chaves[5]:input('Informe a Empresa: '),
            }
                pessoas.append(pessoa)
                continue
            case 2:
                for pessoa in pessoas:
                    print(f'{chaves[0]}: {pessoa[chaves[0]]}')
                    break
