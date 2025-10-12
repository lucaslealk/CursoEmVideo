'''Faça um programa que leia o comprimento do cateto oposto e do 
cateto adjacente de um trângulo retângulo, calcule e mostre 
o comprimento da hipotenusa.'''
import math 
co = float(input('O cateto oposto mede: '))
ca = float(input('O cateto adjacente mede: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

