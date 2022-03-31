from dropshiping.modulos import conta_anuncios
#lista com os produtos/palavra chave que quero buscar
lista_produtos = ['fita led 30cm', 'microfone lapela', 'cadeira giratoria verde',
                  'ring light de mesa', 'apoio encosto lombar', 'lixeira retratil']
#criando as variaveis que desejo armazenar para futura manipulação
lista_true = list()
lista_false = list()
dicionario = dict()
#usando a função lista_produtos para pegar a quantidade de anuncios
for item in lista_produtos:
    #tratando possiveis erros para nenhum produto da lista_produtos serem perdidos de alguma forma
    try:
        dicionario[item] = str(conta_anuncios(item))
        lista_true.append(dicionario.copy())
        dicionario.clear()
    except:
        #caso ocorra um erro no processo o item sera adicionado nesta lista para futuras tomadas de decisão
        lista_false.append(item)
#caso nenhum item tenha sido possivel identificar
if len(lista_false) == len(lista_true) == 0:
    print('\033[33mnão foi possivel identificar nenhum valor\033[m')
else:
    #mostrando de forma formatada todos os itens, tanto os que passaram no try quanto os que deram erro
    print('Os itens disponiveis foram: \n')
    for dicionario in lista_true:
        for chave, valor in dicionario.items():
            print(f'O produto {chave} tem {valor}anuncions online')
    if len(lista_false) == 0:
        print('\033[32mTodos os produtos foram executados com exito\033[m')
    for item in lista_false:
        print(f'\033[31mHouve um erro no sistema em buscar o produto {item}\033[m')


