# 7- Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))

if(numero1 > numero2 and numero2 > numero3):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero1} e o menor entre eles é o número {numero3}!")

elif(numero1 > numero3 and numero3 > numero2):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero1} e o menor entre eles é o número {numero2}!")

elif(numero2 > numero3 and numero1 < numero3):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero2} e o menor entre eles é o número {numero1}!")

elif(numero2 > numero1 and numero3 < numero1):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero2} e o menor entre eles é o número {numero3}!")

elif(numero3 > numero2 and numero1 < numero2):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero3} e o menor entre eles é o número {numero1}!")

elif(numero3 > numero1 and numero2 < numero1):
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. O maior entre eles é o número {numero3} e o menor entre eles é o número {numero2}!")

else:
     print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. Os três são iguais!")

#  CONCLUIDA