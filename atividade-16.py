# 16- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#           - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#           - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#           - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#           - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


valorA = float(input("Usuário, insira o valor de a: "))

if(valorA == 0):
    print(f"O valor digitado foi {valorA}, por isso não pode ser uma equação de segundo grau!")

else:
    valorB = float(input("Usuário, insira o valor de b: "))
    valorC = float(input("Usuário, insira o valor de c: "))
    delta = valorB * valorB - 4 * valorA * valorC
    
    if(delta < 0):
       print(f"O valor de delta foi {delta}, a equação não possui raízes reais.")
    
    elif(delta == 0):
        print(f"O valor de delta foi {delta}, a equação possui apenas uma raiz real: ")
