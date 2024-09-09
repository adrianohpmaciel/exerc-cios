'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''
def calcular_idade():
    while True:
        # Recebe o nome completo do usuário
        nome = input("Digite seu nome completo: ")

        # Tenta receber e validar o ano de nascimento
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))

            # Verifica se o ano está no intervalo válido
            if 1922 <= ano_nascimento <= 2021:
                idade = 2022 - ano_nascimento
                print(f"\nNome: {nome}")
                print(f"Idade que completou/completará em 2022: {idade} anos")
                break
            else:
                print("Erro: O ano deve estar entre 1922 e 2021. Tente novamente.\n")
        except ValueError:
            print("Erro: Por favor, digite um número válido para o ano de nascimento.\n")

# Chama a função para iniciar o programa
calcular_idade()
