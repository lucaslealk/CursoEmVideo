'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
print('Olá, vamos fazer uma brincadeira? Digite três números e eu lhe direi qual é o maior e qual é o menor!')
print(' ')
print('-=-'*20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite o último número: '))

#Verificando o menor número 
menor = n1 
if n2 < n1 and n2 < n3: 
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'Você quer saber qual o menor número? O menor número é: {menor}')

#Verificando o maior número 
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3 
print(f'E o maior número entre os três é: {maior}')

print(' ')
print('-=-'*20)
