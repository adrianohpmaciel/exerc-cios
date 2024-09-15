'''
Copie o array apresentado embaixo no seu editor de código, e imprima no terminal: 
a quantidade de elementos que ele possui, o dado salvo no índice 2, o dado salvo no índice 9, e dado salvo no índice 14.
lista_musicos = [ 
'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 
'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 
'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'] 
'''

lista_musicos = [
    'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento',
    'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso',
    'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'
]

# Armazenando as informações solicitadas
quantidade_elementos = len(lista_musicos)
indice_2 = lista_musicos[2]
indice_9 = lista_musicos[9]
indice_14 = lista_musicos[14]

# Imprimindo os resultados
print("Quantidade de elementos:", quantidade_elementos)
print("Elemento no índice 2:", indice_2)
print("Elemento no índice 9:", indice_9)
print("Elemento no índice 14:", indice_14)
