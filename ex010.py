#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
#Considere US$1,00 = R$ 3,27
valor = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = valor / 3.27
print('Com seu dinheiro R$ {:.2f}, você pode comprar US$ {:.2f} dolares.'.format(valor, dolar))