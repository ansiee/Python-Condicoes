# 11- As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#       - salários até R$ 280,00 (incluindo) : aumento de 20%
#       - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#       - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#       - salários de R$ 1500,00 em diante : aumento de 5% 
#               
#           Após o aumento ser realizado, informe na tela:
#               - o salário antes do reajuste;
#               - o percentual de aumento aplicado;
#               - o valor do aumento;
#               - o novo salário, após o aumento.


salario = float(input("Olá, colaborador! Por favor, insira seu salário para reajuste: "))
salarioReajustado = []
valorAumento = []

if(salario <= 0 and salario < 280):
    salarioReajustado = salario * (1 + 20/100)
    valorAumento = salarioReajustado - salario
    print(f"O seu salário que era de {salario} reais, foi reajustado, com aumento de 20%. O valor do aumento foi de {valorAumento} reais e seu salário novo é {salarioReajustado} reais!")

elif(salario <= 0 and salario >= 280 and salario < 700):
    salarioReajustado = salario * (1 + 15/100)
    valorAumento = salarioReajustado - salario
    print(f"O seu salário que era de {salario} reais, foi reajustado, com aumento de 15%. O valor do aumento foi de {valorAumento} reais e seu salário novo é {salarioReajustado} reais!")

elif(salario <= 0 and salario >= 700 and salario < 1500):
    salarioReajustado = salario * (1 + 10/100)
    valorAumento = salarioReajustado - salario
    print(f"O seu salário que era de {salario} reais, foi reajustado, com aumento de 10%. O valor do aumento foi de {valorAumento} reais e seu salário novo é {salarioReajustado} reais!")

else:
    salarioReajustado = salario * (1 + 5/100)
    valorAumento = salarioReajustado - salario
    print(f"O seu salário que era de {salario} reais, foi reajustado, com aumento de 5%. O valor do aumento foi de {valorAumento} reais e seu salário novo é {salarioReajustado} reais!")

#  CONCLUIDA