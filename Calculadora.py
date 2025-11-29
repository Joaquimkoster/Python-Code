while True:                                                 # se for verdadeiro, significa que ira rodar em loop, sem parar
    
    print("----------------------------")                   # printa uma linha divisoria
    num1 = float(input("digite o primeiro numero: "))       # define a variavel num1, float significa que pode ter casas decimais
    num2 = float(input("digite o segundo numero: "))        # define a variavel num2, float significa que pode ter casas decimais
   
    print("----------------------------")                   # printa uma linha divisoria
    print("Escolha a operação que deseja:")                 # printa o texto e as opções com suas respectivas operações
    print("1) Adição")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")

    op = input("Digite o numero da operação escolhida: ")   # define a variavel op como a operaçao escolhida, input permite poder escolher 

    if op == "1":                                           # if siginifica "se" op for 1, printa resultado com o valor. +
        print("Resultado:", num1 + num2)
    elif op == "2":                                         # elif significa "senão, se" op for 2, printa resultado com o valor. - 
        print("resultado", num2 - num1)           
    elif op == "3":                                         # elif significa "senão, se" op for 3, printa resultado com o valor. * "multiplicação"
        print("resultado:", num1 * num2)                 
    elif op == "4":                                         # elif significa "senão, se" op for 4, printa resultado com o valor. / "divisão"
        print("Resultado:", num1 / num2)
    else:
        print("Operação invalida")                          # else significa "senão", Ele executa quando nenhuma das condições anteriores (if e elif) é verdadeira. ele printa "operaçao invalida"