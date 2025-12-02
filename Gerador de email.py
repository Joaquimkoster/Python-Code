import random

while True:
    print("===== Gerador de Email =====")

    nome = input("Digite seu Nome, Nick que deseja usar: ").lower()

    dominio = ["@gmail.com", "@hotmail.com", "@outlook.com",
           "@yahoo.com", "@live.com", "@icloud.com",
           "@aol.com", "@proton.me", "@protonmail.com",
           "@zoho.com", "@yandex.com", "@mail.com", "@gmx.com"]

    dominio_escolhido = random.choice(dominio)

    resultado = nome + dominio_escolhido

    print(resultado)

    saida = input("Deseja sair? (s/n): ")
    if saida == "s":
        print("Saindo do programa... Obrigado por usar!!")
        break
    elif saida == "n":
        print("Continuando...")
    else:
        ("Opção invalida, tente novamente")

