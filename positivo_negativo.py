#crie uma função que recebe um numero
#e retorna 'P' caso ele for positivo ou 'N'
#caso contrario

def positivo_negativo(numero):
    '''
    Recebe um inteiro e retorna:
    'P' - para numeros positivos
    'N' - para numeros negativos
    '''
    if numero > 0:
        return 'P'
    else:
        return 'N'

#ou depende de se tem um calculo intermediario
#retorno = ''
#if numero = 'P'
#else: retorno = 'N'
#return retorno

a = int(input("Digite um numero"))
print(positivo_negativo(a))