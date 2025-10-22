'''Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão: 
- 1 para binário
- 2 para octal 
- 3  para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão: ')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1: 
    print('O número {} covertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
