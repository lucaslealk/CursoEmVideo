'''Faça um programa que leia um núemro de 0 a 9999 e mostre na tela
cada um dos dígitos separados. 
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10 
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10 
print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('O milhar é: {}'.format(m))
