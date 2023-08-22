# 6- Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))

if(numero1 > numero2 and numero2 > numero3):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero1}!")

elif(numero2 > numero3 and numero3 > numero1):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero2}!")

elif(numero3 > numero2 and numero2 > numero1):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero3}!")
#  CONCLUIDA