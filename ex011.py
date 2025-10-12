'''Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la
, sabendo que cada litro de tinta pinta uma área de 2m².'''
L = float(input('Qual a largura da parede em metros? '))
H = float(input('Qual a altura da parede em metros? '))
A = L * H
T = A / 2
print('A área da parede é de {:.1f}m² e serão necessários {:.1f} litros de tinta para pintar a parede completamente.'.format(A, T))

