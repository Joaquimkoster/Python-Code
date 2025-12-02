import random                                                            # serve para você usar funções que geram números aleatórios ou fazem escolhas aleatórias no Python.


while True:                                                              # inicia o loop
    print("===== Gerador de Email =====")                                # exibe o texto
    nome = input("Digite seu Nome, Nick que deseja usar: ").lower()      # define nome como oque vc digitar

    dominio = ["@gmail.com", "@hotmail.com", "@outlook.com",             # define a variavel dominio, como uma lista de strings
               "@yahoo.com", "@live.com", "@icloud.com",
               "@aol.com", "@proton.me", "@protonmail.com",
               "@zoho.com", "@yandex.com", "@mail.com", "@gmx.com"]

    dominio_escolhido = random.choice(dominio)                           # define dominio_escolhido como uma escolha aleatoria da lista de dominio

    resultado = nome + dominio_escolhido                                 # define resultado como a adição de nome a dominio_escolhido

    print("Seu novo E-mail é",resultado)                                 # exibe o texto, com o resultado

    saida = input("Deseja sair? (s/n): ")                                # define saida como a decisão que vc toma, s ou n
    
    if saida == "s":                                                     # se saida for s, exibe um texto e break para o loop
        print("Saindo do programa... Obrigado por usar!!")
        break
    
    elif saida == "n":                                                   # senão, se saida for n, exibe o texto
        print("Continuando...")
    
    else:                                                                # senão, exibe o texto
        ("Opção invalida, tente novamente")

