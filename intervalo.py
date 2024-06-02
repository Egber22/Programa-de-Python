#leer enterop del teclado
valor = int(input("Digite o numero: "))
#verificar si esta en el intervalo [0,50]
if valor >= 0 and valor <=50:

#si esta, imprime "[0,50"]
    if 0 <= valor <= 50:
        print("0,50")

#Verificar intervalo [51, 100]
elif 51 <= valor <= 100:
     print("[51, 100]")
else:
    print("fora do intervalo")
