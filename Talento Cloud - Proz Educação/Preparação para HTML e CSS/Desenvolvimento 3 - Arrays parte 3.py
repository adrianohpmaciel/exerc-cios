'''
Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram. O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.

Como desafio opcional, tente imprimir cada produto com a frase "Temos [produto] à venda!" (ex. "Temos máscaras faciais à venda!"). 

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
'''
# Array de produtos
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Imprimindo cada produto no terminal
for produto in lista_produtos:
    print(produto)

# Desafio opcional: imprimindo com a frase "Temos [produto] à venda!"
for produto in lista_produtos:
    print(f"Temos {produto} à venda!")

