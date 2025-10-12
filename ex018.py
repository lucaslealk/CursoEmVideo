'''Faça um programa que leia um ângulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse ângulo.'''
import math
ang= float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}!'.format(ang, seno, cosseno, tan))

