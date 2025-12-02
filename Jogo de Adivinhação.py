import random                                                   # serve para você usar funções que geram números aleatórios ou fazem escolhas aleatórias no Python.
numero = random.randint(1, 10)                                  # define a variavel numero, e é uma função do módulo random que gera um número inteiro aleatório entre 1 e 10

print("----- Jogo de adivinhação -----")                        # printa na tela o texto

while True:                                                     # enquanto for verdadeiro, inicia um loop
    escolhido = int(input("Escolha um numero de 1 a 10: "))     # define a variavel numero como o numero q vc digitar, int transforma em numero

    if escolhido > numero:                                      # se escolhido for maior que numero, printa um texto
        print("Esse numero é alto")

    elif escolhido < numero:                                    # se escolhido for menor que numero, printa um texto
        print("Esse numero é baixo")

    elif escolhido == numero:                                   # se escolhido for igual a numero, printa um texto
        print("Correto")
    break                                                       # para o loop