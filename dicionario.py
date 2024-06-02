#dicionario


#conjunto de chaves/valor

# -cada chave é unica
# -uma chave pode ser de varios tipos (int, float, string, tupla....)
# -não é uma lista de valores
# -sempre procurar por chaves, nunca valores

traducoes = {
    'gato':'cat',
    'cachorro':'dog',
    'mesa':'table',
}

numeros = { 'one': 1, 'two': 2, 'three': 3}

print(traducoes)
print(numeros)

#checar se um elemento esta no dicionario usando in e if

#acessar os elementos de um dicionario com for

#keys()
for chave in traducoes.keys():
    print(chave,"->",traducoes[chave])

#itens()
for (chavem, valor) in traducoes.itens():
    print(chave,"->",valor)


#values()
for palavra in traducoes.values():
    print(palavra)

#dicionarios sao mutaveis

#adicionar ou modificar é simples
traducoes['copo'] = 'glass'
traducoes['gato'] = 'kittie'

#remover elemntos
del traducoes['gato']
print(traducoes)