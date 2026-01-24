while True:

    valor1 = float(input("Digite o Primeiro Número: "))
    valor2 = float(input("Digite o Segundo Número: "))
    print("-"*50)
    soma = valor1 + valor2
    print("Soma : ", soma)
    print("-"*50)
    subtracao = valor1 - valor2
    print("Subtracao : ", subtracao)
    print("-"*50)
    if valor2 == 0:
       print('O segundo número da Divisão não pode ser 0')
    else:
       divisao= valor1 / valor2
       print("Divisão: ", divisao)
    print("-"*50)
    multiplicacao =  valor1 * valor2
    print("Multiplicação: ", multiplicacao)
    continua=input('Para sair digite "/sair":  ')
    if continua == '/sair' or "/SAIR":
        break




