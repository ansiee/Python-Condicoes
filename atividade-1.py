# 1- Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))

if(numero1 > numero2):
    print(f"Os números inseridos foram {numero1} e {numero2}, o maior deles é o número {numero1}.")

elif(numero2 > numero1):
    print(f"Os números inseridos foram {numero1} e {numero2}, o maior deles é o número {numero2}.")

else:
    print(f"Os números inseridos foram {numero1} e {numero2}, eles são iguais.")

# CONCLUIDA