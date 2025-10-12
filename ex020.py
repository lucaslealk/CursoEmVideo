'''O mesmo professor do desafio anterior quer sortear a ordem de 
apresentação de trabalho dos alunos. Faça um programa que leia o nome
dos quatro alunos e mostre a ordem sorteada. '''
import random 
a1 = input('O primeiro aluno: ')
a2 = input('O segundo aluno: ')
a3 = input('O terceiro aluno: ')
a4 = input('O quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))

