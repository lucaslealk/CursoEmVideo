'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

valor = float(input('Digite o valor do produto: R$'))
print('Escolha a forma de pagamento:')
print('[ 1 ] À vista dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Em até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    total = valor - (valor * 0.10)
    print(f'O valor a ser pago é R${total:.2f} com 10% de desconto.')
elif opcao == 2:
    total = valor - (valor * 0.05)
    print(f'O valor a ser pago é R${total:.2f} com 5% de desconto.')
elif opcao == 3:
    total = valor 
    parcela = total / 2
    print(f'O valor a ser pago é R${total:.2f} em 2x de R${parcela:.2f} sem juros.')
elif opcao == 4:
    total = valor + (valor * 0.20)
    num_parcelas = int(input('Digite o número de parcelas (até 12): '))
    parcela = total / num_parcelas
    print(f'O valor a ser pago é R${total:.2f} em {num_parcelas}x de R${parcela:.2f} com 20% de juros.') 