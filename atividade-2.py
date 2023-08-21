# 2- Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Insira um número: "))

if(numero < 0):
    print(f"O número {numero} que foi inserido, corresponde a um número NEGATIVO!")

elif(numero > 0):
    print(f"O número {numero} que foi inserido, corresponde a um número POSITIVO!")

else:
    print(f"O número {numero} que foi inserido, corresponde a um número NULO!")