#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
print('Vamos somar apenas os números pares que você digitar, ENTÃO CAPRICHA!')
soma = 0

for n in range(1, 7):
	num = int(input(f'Digite o {n}º número: '))
	if num % 2 == 0:
	    soma += num
print(f'A soma dos números pares é: {soma}')