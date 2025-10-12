'''Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações 
possíveis sobre ele.'''
n = input('Digite o que quiser: ')
print('O tipo primitivo desse bagui é', type(n))
print('É um número?', n.isnumeric())
print('É um alfanúmerico?', n.isalnum())
print('É alfabeto?', n.isalpha())
print('Tem espaços?', n.isspace())
print('Está maiúsculo?', n.isupper())
print('Está minúsculo?', n.islower())
print('Está capitalizada?', n.istitle())
print('É decimal?', n.isdecimal())
print('É dígito?', n.isdigit())
print('É um identificador?', n.isidentifier())
print('É imprimível?', n.isprintable())
