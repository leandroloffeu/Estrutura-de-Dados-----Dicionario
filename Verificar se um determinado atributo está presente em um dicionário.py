dicionario = {
'nome':'leandro',
'idade': 'sem informações',
'endereço':'Maricá',
'telefone':'(21) 99999-9999',
}

v = str(input('digite um atributo para verificar no dicionário:'))

if v in dicionario:
    print(f'existe')
else:
    print(f'não existe')