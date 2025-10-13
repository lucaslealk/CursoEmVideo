#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
#ou
print('Seu nome tem Silva? {}'.format(nome.upper().find('SILVA') != -1))