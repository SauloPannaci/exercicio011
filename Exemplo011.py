"""
Exercicio - complementar o exemplo011. 
Adicionar um novo atributo referente a quantidade do produto e em seguida desenvolver a funcionalidade 3 - Consultar Valor Total do Estoque, que deve ser calculada qtd_prod_1 X preco_prod_1 + qtd_prod_2 x preco_prod_2 +...+ qtd_prod_n X preco_prod_n
"""
opcao = 1
bd_estoque = []    
while opcao != 4:
    print('='*10)
    print("1- Adicionar")
    print('2- Consultar estoque')
    print('3- Consultar Valor Total do Estoque')
    print('4- Sair')
    opcao = int(input('Opcao >>>> '))
    if opcao == 1:
        print('-----Adicionar produto-----')
        codigo = int(input('Codigo: '))
        nome = input('Nome: ')
        descricao = input('Descricao: ')
        preco = float(input('Preco: R$ '))
        produto = [codigo, nome, descricao, preco]
        bd_estoque.append(produto) 
        print('-----Adicionado com sucesso-----')
    elif opcao == 2:
        print('-----Estoque-----')
        print(bd_estoque)
        print('Codigo\tNome\tDescricao\tPreco')
        for prod in bd_estoque:
            print(prod[0],end='\t')   
            print(prod[1],end='\t')
            print(prod[2],end='\t')
            print(prod[3])
        print('-----Fim estoque-----')
    elif opcao == 3:
        pass   
    elif opcao == 4:
        print('saindo....')
    else:
        print('opcao incorreta')