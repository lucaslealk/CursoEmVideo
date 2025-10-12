'''Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia 
e R$0,15 por km rodado.'''
km = float(input('Quantos km foram percorridos? '))
d = int(input('Por quantos dias o carro foi alugado? '))
p = (60 * d) + (0.15 * km)
print('O valor total a pagar é de R${:.2f}'.format(p))

