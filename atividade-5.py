# 5- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#       - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#       - A mensagem "Reprovado", se a média for menor do que sete;
#       - A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))

media = (nota1 + nota2) / 2

if (media <= 6):
    print(f"Sua média foi {media} pontos. Você foi REPROVADO!! Estude mais um pouco :/.")

elif (media == 10):
    print(f"Sua média foi de {media} pontos. Você foi APROVADO com DISTINÇÃO. Parabéns!!! :)")

else:
    print(f"Sua média foi de {media} pontos. Você foi APROVADO. Parabéns!!! :)")