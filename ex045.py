'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import choice
from time import sleep 
from cores import cores 
itens = ('pedra', 'papel', 'tesoura')
computador = choice(itens)
print('==' * 20)
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL 
      [ 2 ] TESOURA''')
jogador = int(input('Faça a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('==' * 20)
print(f'O computador jogou {computador}')
if jogador == 0:
    print('Você jogou pedra')
elif jogador == 1:
    print('Você jogou papel')
elif jogador == 2:
    print('Você jogou tesoura')
else:
    print('Jogada inválida! Você perdeu!')
    exit()
print('==' * 20)
if computador == 'pedra':
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
elif computador == 'papel':
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
elif computador == 'tesoura':
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
print('==' * 20)

