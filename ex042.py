'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de 
mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''
n1 = int(input('Digite o comprimento da primeira reta: '))
n2 = int(input('Digite o comprimento da segunda reta: '))
n3 = int(input('Digite o comprimento da terceira reta: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('As retas acima podem formar um triângulo!')
    if n1 == n2 == n3:
        print('O triângulo é do tipo EQUILÁTERO pois todos os lados são iguais.')
    elif n1 != n2 != n3 != n1:
        print('O triângulo é do tipo ESCALENO pois todos os lados são diferentes.')
    else:
        print('O triângulo é do tipo ISÓCELES pois dois lados são iguais.')
else:
    print('As retas acima não pode formar um triângulo!')
