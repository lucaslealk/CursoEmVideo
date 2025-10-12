#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o preço do produto: R$'))
desconto = produto * 0.05
novo_preco = produto - desconto
print('O preço do produto com 5% de desconto é R${:.2f}'.format(novo_preco))
