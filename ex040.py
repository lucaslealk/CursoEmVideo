'''Crie um progrma que leia duas notas de um aluno e cacule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado'''
from cores import cores 
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua média foi {:.1f}. Você está {}REPROVADO{}.'.format(media, cores['vermelho'], cores['reset']))
elif 5.0 <= media <= 6.9:
    print('Sua média foi {:.1f}. Você está de {}RECUPERAÇÃO{}.'.format(media, cores['amarelo'], cores['reset']))
else:
    media >= 7.0
    print('Sua média foi {:.1f}. Você está {}APROVADO{}!'.format(media, cores['verde'], cores['reset']))
