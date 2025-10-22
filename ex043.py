'''Desenvolva um programa que leia o peso e altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros (ex:1.60): '))

imc = peso / (altura * altura) 

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Você está com OBESIDADE')
else:
    imc >= 40 
    print(f'Seu IMC é {imc:.1f}. Você está com OBESIDADE MÓRBIDA. CUIDADO!')


