#Escreva um programa que converta uma temperatura digitada em °C e converta para °F. 
C = float(input('Digite a temperatura em °C: '))
F = (C * 1.8) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(C, F))
