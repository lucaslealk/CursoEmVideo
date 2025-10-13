# Manipulação de strings
frase = 'Curso em Vídeo Python'
print(frase[:21])
print(frase[13:21])
print(frase.capitalize())
print(frase.upper())
print(frase.lower())
print(len(frase))
print(frase.count('o'))
frase = frase.replace('Python', 'Facebook')
print(frase)
print(frase.split())
print('/'.join(frase))
print(frase.find('Vídeo'))
