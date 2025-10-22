'''A confederação brasileira de natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo 
com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima de 20 anos: MASTER'''

from datetime import date
from cores import cores

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print(f'O atleta de {idade} anos é da categoria {cores['amarelo']}MIRIM{cores['reset']}.')
elif idade <= 14:
    print(f'O atleta de {idade} anos é da categoria {cores['verde']}INFANTIL{cores['reset']}.')
elif idade <= 19:
    print(f'O atleta de {idade} anos é da categoria {cores['azul']}JÚNIOR{cores['reset']}.')
elif idade <= 20:
    print(f'O atleta de {idade} anos é da categoria {cores['roxo']}SÊNIOR{cores['reset']}')
else:
    print('O atleta de {} anos é da categoria {}MASTER{}.'.format(idade, cores['vermelho'], cores['reset']))

