# 8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Insira o preço do primeiro produto:"))
produto2 = float(input("Insira o preço do segundo produto:"))
produto3 = float(input("Insira o preço do terceiro produto:"))

if(produto1 < produto2 and produto1 < produto3):
    print(f"Os preços inseridos foram: Produto 1 - {produto1} reais, Produto 2 - {produto2} reais e Produto 3 - {produto3} reais. O produto que se deve comprar é o Produto 1 com o preço de {produto1} reais, pois é o mais barato!")

elif(produto2 < produto1 and produto2 < produto3):
    print(f"Os preços inseridos foram: Produto 1 - {produto1} reais, Produto 2 - {produto2} reais e Produto 3 - {produto3} reais. O produto que se deve comprar é o Produto 2 com o preço de {produto2} reais, pois é o mais barato!")


elif(produto3 < produto1 and produto3 < produto2):
    print(f"Os preços inseridos foram: Produto 1 - {produto1} reais, Produto 2 - {produto2} reais e Produto 3 - {produto3} reais. O produto que se deve comprar é o Produto 3 com o preço de {produto3} reais, pois é o mais barato!")

else:
    print(f"Os preços inseridos foram: Produto 1 - {produto1} reais, Produto 2 - {produto2} reais e Produto 3 - {produto3} reais. Os três produtos tem o mesmo preço!")