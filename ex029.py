'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.'''
vel = float(input('Qual é a velocidade atual do carro? KM '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h')
    print(f'Você vai pagar uma multa de R${multa:.2f}')
    