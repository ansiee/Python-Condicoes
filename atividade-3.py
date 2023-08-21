# 3- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = str(input("Insira seu sexo (F ou M): "))

if(letra == 'F' or letra == 'f'):
    print(f"Você escreveu {letra}, logo, seu sexo é FEMININO!")

elif(letra == 'M' or letra == 'm'):
    print(f"Você escreveu {letra}, logo, seu sexo é MASCULINO!")

else:
    print(f"Você escreveu {letra}, logo, seu sexo é INVÁLIDO!")