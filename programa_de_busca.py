

# Laço de repeção
sair = False
lista = ['jonas', 'clarisse','Paulo', 'Joao','felipe','marcus','Hiago']
while sair == False :

    
    print("___Menus___")
    print('( 1 ) Mostra lista')
    print('( 2 ) Adicionar nome')
    print('( 3 ) Pesquisar nome')
    print('( 4 ) Remover nome')
    print('( 5 ) Finalizar')
    #Entra para escolha do menu e suas condições
    escolha = int(input('Opção do Menu: '))

    # Mostra nomes da lista
    if escolha == 1:
        for n in lista:
            print(f'Nome: {n}')
        print(f'Total: {len(lista)}')
    
    # Add novo nome
    elif escolha == 2:
        add = input('Adicionar Nome: ').capitalize().strip()
        print(add)
        lista.append(add)
    
    # Pesquisar lista
    elif escolha == 3:
        busca = input('Pesquisar nome: ')
        nome = busca in lista
        if nome == True:
            print(f'Nome: {busca}')
        else:
            print(f'{busca} não encontrado')
        s = input('Fazer nova busca? S/N:').upper().strip()
        if s == 'N':
            print('Fim do Programa!')
            sair = True

    # Remover nome
    elif escolha == 4:
        busca = input('Remover NOME: ')
        nome = busca in lista
        if nome == True:
            lista.remove(busca)
            print(f'{busca} removido com sucesso!')
        else:
            print(f"Nome {busca} não esta na lista")

    # Finalizar programa
    elif escolha == 5:
        print('Fim do programa!')
        break

