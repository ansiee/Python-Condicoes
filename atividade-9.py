# 8- Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))

if(numero1 < numero2 and numero2 < numero3):
    print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. A ordem descrescente desses números é {numero3}, {numero2} e {numero1}.")

elif(numero2 > numero1 and numero3 < numero1):
    print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. A ordem descrescente desses números é {numero2}, {numero1} e {numero3}.")

elif(numero3 < numero1 and numero2 < numero1):
    print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. A ordem descrescente desses números é {numero1}, {numero3} e {numero2}.")

else:
    print(f"Os números inseridos foram {numero1}, {numero2} e {numero3}. E os três sao iguais!")

#  CONCLUIDA