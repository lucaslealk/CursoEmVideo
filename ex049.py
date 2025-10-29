#Refaça DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número para ver a tabuada: '))
print(f'\n A tabuada de {n} é: ')
print('-' * 12)
for multiplicador in range(1, 11):
    print('{} x {:2} = {}'.format(n, multiplicador, resultado := n * multiplicador))
print('-' * 12)