dicionario = {
'nome':'leandro',
'idade': 'sem informações',
'endereço':'Maricá',
'telefone':'(21) 99999-9999',
}

print (dicionario)

novo = str(input('digite um novo nome para o dicionário: '))
dicionario['nome'] = novo

print(dicionario)