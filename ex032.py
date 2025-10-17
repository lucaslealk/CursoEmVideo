'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
# Um ano é bissexto quando for divisível por 4 e não for divisível por 100. Em casos de terminar com 00, só será bissexto se divisível por 400. 
