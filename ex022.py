'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas minúsculas. 
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome fica assim com o maiúsculas: ',nome.upper())
print('Seu nome fica assim com o minúsculas: ',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))

  