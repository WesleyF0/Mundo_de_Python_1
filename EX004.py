algo = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(algo)))
print('Só tem espaços? ', algo.isspace())
print('É númerico? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print ('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minúsculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle()) # É diferente do isidentifer...

