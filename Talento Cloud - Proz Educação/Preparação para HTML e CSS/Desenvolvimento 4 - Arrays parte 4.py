'''
A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! 
Dessa vez, eles precisam que você atualize o array de produtos. 
Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. 
Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. 
Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista. 
'''
# Array de produtos original
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Atualizando o array de produtos
lista_produtos[1] = 'rímel'  # Substituindo batons por rímel
lista_produtos[4] = 'cremes hidratantes'  # Substituindo loções por cremes hidratantes
lista_produtos.remove('delineadores')  # Removendo delineadores

# Desafio opcional: Adicionando dois novos produtos
lista_produtos.append('protetor solar')
lista_produtos.append('condicionador')

# Imprimindo a nova lista de produtos
print(lista_produtos)
