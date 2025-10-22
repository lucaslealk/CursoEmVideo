'''Escreva um programa para aprovar o empréstimo bancário para a 
compra de uma casa. O programa vai perguntar o valor da casa, 
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode 
exceder 30% do salário ou então o empréstimo será negado.''' 

import cores

valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos ele pretende pagar? '))

prestacao = valor_casa / (anos * 12)

if prestacao * 100 / salario > 30:
    print('Seu empréstimo foi {}NEGADO{} pois a prestação mensal de R${:.2f}, excedeu 30% do seu salário.'.format(cores.cores['vermelho'], cores.cores['reset'], prestacao))
else:
    print('Seu empréstimo foi {}APROVADO{}! A prestação mensal será de R${:.2f}.'.format(cores.cores['verde'], cores.cores['reset'], prestacao))

