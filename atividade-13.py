# 13- Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Olá usuário, insira o número do dia da semana: "))

if(numero == 1):
    print(f"O número digitado foi {numero}, o dia da semana que corresponde a esse número é DOMINGO.")

elif(numero == 2):
    print(f"O número digitado foi {numero}, o dia da semana que corresponde a esse número é SEGUNDA-FEIRA.")

elif(numero == 3):
    print(f"O número digitado foi {numero}, o dia da semana que corresponde a esse número é TERÇA-FEIRA.")

elif(numero == 4):
    print(f"O número digitado foi {numero}, o dia da semana que corresponde a esse número é QUARTA-FEIRA.")

elif(numero == 5):
    print(f"O número digitado foi {numero}, o dia da semana que corresponde a esse número é QUINTA-FEIRA.")

elif(numero == 6):
    print(f"O número digitado foi {numero}, o dia da semana que corresponde a esse número é SEXTA-FEIRA.")

elif(numero == 7):
    print(f"O número digitado foi {numero}, o dia da semana que corresponde a esse número é SÁBADO.")

else:
    print(f"O número {numero} é inválido, por favor, insira um dos números válidos. (1- Domingo, 2- Segunda-feira, 3- Terça-feira, 4- Quarta-feira, 5- Quinta-feira, 6- Sexta-feira e 7- Sábado.)")