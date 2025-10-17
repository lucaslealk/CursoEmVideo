'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é ÍMPAR!')
# % é o operador módulo, que retorna o resto da divisão. Se o resto da divisão por 2 for 0, o número par. Se for 1, é ímpar.
