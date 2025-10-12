#Faça um programa que leia um núemro inteiro qualquer e mostre na tela a sua tabuada. 
n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
#inicia um laço que vai do 1 a o 10
for multiplicador in range(1, 11):
    #calcula o resultado da multiplicação
    #resultado = n * multiplicador
    #mostra o resultado formatado
    print('{} x {:2} = {}'.format(n, multiplicador, resultado := n * multiplicador))
print('-' * 12)




