# 10- Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input("Aluno, antes de entrar no sistema, insira o turno em que você estuda, sendo M para matutino, V para vespertino e N para noturno: "))

if(turno == 'm' or turno == 'M'):
    print(f"Bom dia, aluno! Você entrou no sistema.")

elif(turno == 'v' or turno == 'V'):
    print(f"Boa tarde, aluno! Você entrou no sistema.")

elif(turno == 'n' or turno == 'N'):
    print(f"Boa noite, aluno! Você entrou no sistema.")

else:
    print(f"Turno inválido! Insira novamente.")

#  CONCLUIDA