# 4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Insira uma letra: "))

if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print(f"A letra {letra} é uma VOGAL!")

else: 
    print(f" A letra {letra} é uma CONSOANTE!")