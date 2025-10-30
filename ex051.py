#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('\nVamos calcular uma Progressão Aritimética!')
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
na = n1 + (11 - 1) * r
for c in range(n1, na, r):
    print(f'{c}', end = ' -> ')
print('FIM')
