#leer el nombre de la primera persona
primer_nombre = input("Digite el nombre de la primera persona: ")

#leer la edad de la primera persona
primera_edad = int(input("Digite ka edad de la primera persona: "))

#leer el nombre de la segunda persona
segundo_nombre = input("Digite el nombre de la segunda persona: ")

#leer edad de la segunda persona
segunda_edad = int(input("Digite la edad de la segunda persona: "))

#imprimir el nombre del mas viejo

if primera_edad > segunda_edad:
    print(primer_nombre)
        
else:
     print(segundo_nombre)