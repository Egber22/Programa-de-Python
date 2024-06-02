#erros de compilação / erros de parsing
import sys
#erros em tempos de execução -> Exceções

def fsimples(b):
    a = 1/0

def outrafuncao(a):
    fsimples(a)


#try/except/finally

try:
    a = int(input())
    outrafuncao(a)
    print("Tudo certo")
except ZeroDivisionError:
    print("Não é permitida a dividão po zero")
except ValueError:
    print("Use apenas numeros")
finally:
    print("sempre apareço")