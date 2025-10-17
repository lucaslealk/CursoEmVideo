'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
n1 = int(input('Digite o comprimento da primeira reta: '))
n2 = int(input('Digite o comprimento da segunda reta: '))
n3 = int(input('Digite o comprimento da terceira reta: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('As retas acima podem formar um triângulo!')
else:
    print('As retas acima não pode formar um triângulo!')
