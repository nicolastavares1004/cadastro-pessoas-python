def ler_pessoas(nome_arquivo):
    with open(f'{nome_arquivo}','r', encoding='utf-8') as arquivo:
        pessoa, pessoas = {}, []
        for c, linha in enumerate(arquivo):
            dados = linha.strip()
            if c%3==0:
                pessoa['nome'] = dados
            elif c%3==1:
                pessoa['idade'] = int(dados)
            else:
                pessoa['cidade'] = dados
                pessoas.append(pessoa)
                pessoa = {}
    return pessoas
pessoas = ler_pessoas('pessoas.txt')

def mostrar_pessoas(pessoas):
    for pessoa in pessoas:
        print(f'Nome: {pessoa['nome']}')
        print(f'Idade: {pessoa['idade']}')
        print(f'Cidade: {pessoa['cidade']}')
        print('-'*20)

def adicionar_pessoa(pessoas):
    pessoa = {}
    pessoa['nome'] = input('Nome:')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['cidade'] = input('Cidade: ')
    pessoas.append(pessoa)
    return pessoas

def alterar_pessoas(pessoas, nome):
    encontrou = False
    idade_nova = int(input('Nova idade: '))
    cidade_nova = input('Nova cidade: ')
    for pessoa in pessoas:
        if nome == pessoa['nome']:
            pessoa['idade'] = idade_nova
            pessoa['cidade'] = cidade_nova
            encontrou = True
    if encontrou:
        return pessoas
    else:
        print('Não encontrado! ')
        return pessoas

def excluir_pessoa(pessoas, nome):
    for c, pessoa in enumerate(pessoas):
        if pessoa['nome'] == nome:
            del pessoas[c]
            return pessoas  
    print('Pessoa não encontrada')
    return pessoas

def salvar_pessoas(nome_arquivo, pessoas):
    with open(f'{nome_arquivo}','w',encoding='utf-8') as arquivo:
        for pessoa in pessoas:
            arquivo.write(f'{pessoa['nome']}\n')
            arquivo.write(f'{pessoa['idade']}\n')
            arquivo.write(f'{pessoa['cidade']}\n')



opção = 0
while opção != 5:
    opção = int(input('====== CADASTRO DE PESSOAS ======\n1 - Mostrar pessoas\n2 - Adicionar pessoa\n3 - Alterar pessoa\n4 - Excluir pessoa\n5 - Sair\n==========================\n'))
    if opção == 1:
        mostrar_pessoas(pessoas)

    elif opção == 2:
        pessoas = adicionar_pessoa(pessoas)
        

    elif opção == 3:
        pessoas = alterar_pessoas(pessoas,input('Digite o Nome de quem quer alterar: '))

    elif opção == 4:
        pessoas = excluir_pessoa(pessoas,input('Digite o Nome de quem quer excluir: '))
salvar_pessoas('pessoas.txt',pessoas)    
    