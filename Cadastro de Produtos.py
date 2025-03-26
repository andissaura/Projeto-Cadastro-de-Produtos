def listar_produtos():
    """
    Lista todos os produtos cadastrados e suas informações.

    Caso não tenha nenhum produto, exibe uma mensagem informativa.

    Returns:
        None
    """
    # Verifica se a lista está vazia
    if not produtos:
        print('Nenhum produto cadastrado.')
    else:
        for i, produto in enumerate(produtos, start=1):
            print('-' * 20)
            print(f'Produto nº {i}')
            print(
                f"Produto: {produto['Produto'].capitalize()} \n"
                f"Preço: {produto['Preço']} \n"
                f"Quantidade: {produto['Quantidade']}"
            )
            print('-' * 20)

def menu_principal():
    """
    Exibe as opções do menu principal para o usuário escolher sua ação.

    Returns:
        str: A escolha do usuário.
    """
    escolha = 0 # Inicializando a var de escolha

    # Menu Principal
    while True:
        print('|1| Cadastrar um novo produto')
        print('|2| Listar produtos cadastrados')
        print('|3| Buscar produto pelo nome')
        print('|4| Atualizar um produto')
        print('|5| Remover produto')
        print('|6| Encerrar o programa')
        print('')

        # Validação num da ação
        try:
            escolha = int(input('Digite o número da ação desejada: '))
            if escolha < 1 or escolha > 6: # Garante um num de 1 a 6
                print('Escolha um número entre 1 e 6. Tente novamente.')
                print('')
                continue
            break
        except ValueError:
            print('Escolha um número válido. Tente novamente.')
            print('')
            continue
    return escolha # Retorna a escolha do usuário

def menu_pos(acao):
    """
    Exibe um menu pós ação do usuário.

    Args:
        acao (str): Ação que o usuário gostaria de realizar (Ex: Cadastrar, remover...)

    Returns:
        str: A escolha do usuário em continuar ou voltar.
    """
    while True:
        print(f'|1| {acao} outro produto')
        print('|2| Voltar ao menu principal')

        # Validação da ação
        try:
            opcao = int(input('O que você deseja fazer agora? '))
            print('-' * 20)
            print('')
            if opcao == 1:
                return 'continuar'
            elif opcao == 2:
                return 'voltar'
            else: # Caso digite outro num que não 1 ou 2
                print('Escolha a opção 1 ou 2. Tente novamente.')
                print('')
        except ValueError: # Caso não digite um num
            print('Número inválido. Tente novamente.')
            print('')

def add_produto():
    """
    Solicita as informações de nome, preço e quantidade do novo produto.
    Cria um dicionário para ele e adiciona na lista de produtos.

    Returns:
        None
    """
    # Tratamento nome do produto
    while True:
        novoProd = input('Insira o nome do produto: ').strip().lower()
        if not novoProd:
            print('Preencha o nome do produto, o campo não pode estar vazio.')
            print('')
            continue

        if any (p['Produto'] == novoProd for p in produtos):
            print('Erro: Produto já cadastrado.')
            print('')
            continue
        break

    # Tratamento valor
    while True:
        try:
            valorProd = float(input('Insira o valor do produto: '))
            break
        except ValueError:
            print('Insira um número válido.')
            print('')

        # Tratamento qtd
    while True:
        try:
            qtdProd = int(input('Insira a quantidade: '))
            break
        except ValueError:
            print('Insira um número válido.')
            print('')

    # Cria um novo dict para o produto
    novo_produto = {
        'Produto': novoProd,
        'Preço': valorProd,
        'Quantidade': qtdProd
    }

    # Adiciona o dict na lista de produtos
    produtos.append(novo_produto)
    print('Produto adicionado com sucesso!')
    print('')
    print('-' * 20)

def buscar_produto():
    """
    Recebe o nome do produto e efetua uma busca na lista de dicionários.
    Se encontrado, exibe suas informações. Se não encontrado, exibe uma
    mensagem informativa.

    Returns:
         None
    """
    while True:
        buscarProd = str(input('Digite o nome do produto para buscar: ')).strip().lower()
        if not buscarProd:
            print('Insira o nome do produto, o campo não pode estar vazio.')
            print('')
            continue
        break

    encontrado = False  # VAR de controle

    # Procura o dict do produto na lista, iniciando com 1
    for i, produto in enumerate(produtos, start=1):
        if buscarProd in produto['Produto']:
            print('-' * 20)
            print(f'Produto nº {i}')
            print(
                f"Produto: {produto['Produto'].capitalize()} \n"
                f"Preço: {produto['Preço']} \n"
                f"Quantidade: {produto['Quantidade']}"
            )
            print('-' * 20)
            encontrado = True  # Marca que o produto foi encontrado

    if not encontrado:  # Se não houver o produto cadastrado
        print('Produto não encontrado. Tente novamente')
        print('')

def atualizar_produto():
    """
    Recebe a informação de qual produto o usuário deseja alterar, e oferece
    a opção para alterar valor ou quantidade.
    Caso não encontre o produto na lista de produtos, exibe uma mensagem.

    Returns:
        None
    """
    print('')
    encontrado = False

    # Valida se o usuário preencheu o nome do produto
    while True:
        buscarProd = str(input('Digite o nome do produto para alterar: ')).strip().lower()
        if not buscarProd:
            print('Digite o nome do produto, o campo não pode estar vazio.')
            print('')
            continue
        break
    print('')

    # Busca o dict na lista de produtos
    for produto in produtos:
        if buscarProd in produto['Produto']:
            encontrado = True # Marca que o prod foi encontrado
            print('Produto encontrado!')
            print('-' * 20)
            print(
                f"Produto: {produto['Produto'].capitalize()} \n"
                f"Preço: {produto['Preço']} \n"
                f"Quantidade: {produto['Quantidade']}"
            )
            print('-' * 20)
            print('')

            # Solicita o que será alterado
            print('|1| Alterar o valor')
            print('|2| Alterar a quantidade')
            print('')

            # Valida se inseriu um num
            while True:
                try:
                    escolha = int(input('O que você quer alterar? '))
                    if escolha < 1 or escolha > 2:  # Valida se escolherá um num válido
                        print('Escolha 1 ou 2. Tente novamente.')
                        continue
                    break
                except ValueError:
                    print('Insira um número válido. Tente novamente')
                    print('')
            if escolha == 1:  # Alterar o valor
                while True:
                    try: # Validação de num válido
                        novoVal = float(input('Digite o novo valor: '))
                        produto['Preço'] = novoVal
                        print('')
                        print('Preço alterado com sucesso!')
                        print('')
                        break
                    except ValueError:
                        print('Insira um número válido.')
                        print('')
            elif escolha == 2: # Alterar a quantidade
                while True:
                    try:
                        novaQtd = int(input('Digite a nova quantidade: '))
                        produto['Quantidade'] = novaQtd
                        print('Quantidade alterada com sucesso!')
                        break
                    except ValueError:
                        print('Insira um número válido.')
                        print('')
            break

    if not encontrado:  # Se o prod não for encontrado
        print('Produto não encontrado. Tente novamente')
        print('')

def remover_produto():
    """
    Recebe o nome do produto para remoção e remove da lista o dicionário referente
    ao produto.
    Caso o produto não esteja cadastrado, ele exibe uma mensagem informando.

    Returns:
         None
    """
    print('')
    while True:
        nomeProd = str(input('Digite o nome do produto para remover: ')).strip().lower()
        if not nomeProd: # Valida se o campo não está vazio
            print('Insira o nome do produto, o campo não pode estar vazio.')
            print('')
            continue
        break
    print('')

    encontrado = False  # VAR de controle

    for produto in produtos:
        if nomeProd in produto['Produto'].lower():
            encontrado = True  # Marca que o prod foi encontrado
            print('Produto encontrado!')
            print('-' * 20)
            print(
                f"Produto: {produto['Produto'].capitalize()} \n"
                f"Preço: {produto['Preço']} \n"
                f"Quantidade: {produto['Quantidade']}"
            )
            print('-' * 20)

            # Confirma a remoção
            while True:
                confirm = input(
                    f'Tem certeza que deseja remover {produto["Produto"].capitalize()}? (S/N): '
                ).strip().lower()
                if not confirm:
                    print('O campo não pode estar vazio, insira S ou N.')
                    print('')
                    continue
                elif confirm == 's':
                    produtos.remove(produto)  # Remove dict da lista
                    print('Produto removido com sucesso!')
                    print('')
                    break
                elif confirm == 'n':
                    print('Remoção não realizada.')
                    print('')
                    break
                else: # Se digitar outra coisa que não S ou N
                    print('Resposta inválida. Insira S para SIM ou N para NÃO.')
                    print('')
                    continue

    if not encontrado:  # Se o produto não for encontrado
        print('Produto não encontrado. Tente novamente')
        print('')


# Título Inicial
print('-'*45)
print('-'*7, 'SISTEMA DE CADASTRO DE PRODUTO', '-'*7)
print('-'*45)

# Lista de produtos, que irá conter um dict pra cada produto.
produtos = []

while True:
    escolha = menu_principal()

    # Cadastrar novo produto
    if escolha == 1:
        print('')
        print('-' * 37)
        print('-' * 7, 'CADASTRAR NOVO PRODUTO', '-' * 7)
        print('-' * 37)

        while True:
            add_produto()

            # Chamada do menu pós ação
            acao = menu_pos('Adicionar')
            if acao == 'continuar':
                continue # Remover outro produto
            elif acao == 'voltar':
                break # Retorna ao menu principal


    # Listar todos os produtos
    elif escolha == 2:
        listar_produtos()

        # Menu pós listagem
        print('')
        print('|1| Voltar ao menu principal')
        print('|2| Sair do programa')
        print('')

        # Valida se irá inserir um número
        try:
            opcao = int(input('O que você deseja fazer agora? '))
            print('-' * 20)
            print('')
            if opcao < 1 or opcao > 2: # Valida se escolherá uma opção válida
                print('Escolha a opção 1 ou 2. Tente novamente.')
                print('')
            elif opcao == 1:
                continue
            elif opcao == '2':
                print('Até a próxima!')
                break
        except ValueError:
            print('Insira um número válido. Tente novamente.')
            print('')

    # Buscar produto por nome
    elif escolha == 3:
        print('')
        print('-' * 37)
        print('-' * 11, 'BUSCA POR NOME', '-' * 11)
        print('-' * 37)

        while True:
            buscar_produto()

            # Chamada do menu pós ação
            acao = menu_pos('Buscar')
            if acao == 'continuar':
                continue # Remover outro produto
            elif acao == 'voltar':
                break # Retorna ao menu principal

    # Atualizar um produto
    elif escolha == 4:
        print('')
        print('-' * 40)
        print('-' * 9, 'ALTERAÇÃO DE PRODUTO', '-' * 9)
        print('-' * 40)

        # Lista todos os produtos para o usuário
        listar_produtos()

        while True:
            atualizar_produto()

            # Chamada do menu pós ação
            acao = menu_pos('Atualizar')
            if acao == 'continuar':
                continue # Remover outro produto
            elif acao == 'voltar':
                break # Retorna ao menu principal

    # Remover produto
    elif escolha == 5:
        print('')
        print('-' * 40)
        print('-' * 9, 'REMOÇÃO DE PRODUTO', '-' * 9)
        print('-' * 40)

        while True:
            remover_produto()

            # Chamada do menu pós ação
            acao = menu_pos('Remover')
            if acao == 'continuar':
                continue # Remover outro produto
            elif acao == 'voltar':
                break # Retorna ao menu principal

    # Encerrar o programa
    elif escolha == 6:
        print('Encerrando, até a próxima!')
        break