'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, 
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.'''
dis = float(input('Qual é a distância da sua viagem? KM '))
if dis <= 200: 
    preço = dis * 0.50
else:
    preço = dis * 0.45
print(f'O preço da sua passagem será de R${preço:.2f}')
