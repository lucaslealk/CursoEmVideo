'''Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade:
-Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou
do prazo.'''
from datetime import date
import cores 
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    anos_faltando = 18 - idade
    print('Você ainda vai se alistar ao serviço militar. Faltam {}{}{} ano(s).'.format(cores.cores['verde'], anos_faltando, cores.cores['reset']))
    print('Seu alistamento será em {}{}{}'.format(cores.cores['amarelo'], ano_atual + anos_faltando, cores.cores['reset']))
elif idade == 18:
    print('Está na hora do seu alistamento ao serviço militar!')
else:
    anos_passados = idade - 18 
    print('Você já deveria ter se alistado ao serviço militar há {}{}{} ano(s).'.format(cores.cores['vermelho'], anos_passados, cores.cores['reset']))
    print('Seu alistamento deveria ter sido em {}{}{}!'.format(cores.cores['ciano'], ano_atual - anos_passados, cores.cores['reset']))