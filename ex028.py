'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o 
número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu'''
from  random import randint

computador = randint(0, 5) #Faz o computador "pensar"
print('-=-'*20)
print(' ')
print('Vou pesar em um número entre 0 e 5. Tente adivinhar...')
print(' ')
print('-=-'*20)

jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('É ISSO AÍ! Você me venceu!')
else:
    print(f'HAHAHA! Eu venci! Eu pensei no número {computador} e não no {jogador}!')
    print(' ')
    print('--- FIM ---')