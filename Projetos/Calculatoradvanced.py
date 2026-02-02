#raiz quadrada, 1 aplicação da lib math
import math

def raiz_quadrada():
    print("-"*30)


    numero = float(input(f"O número para a raiz quadrada: \n"))
    raiz = math.sqrt(numero)
    print("Resultado: " + str(raiz))



#somar 3 números
def somar3_numeros():
    print("-" * 30)

    resultado = 0
    contador = 1
    for entrada in range(1,4):
        entrada = int(input(f"O {contador} número é: "))
        resultado += entrada
        contador += 1
    print("O resultado é: ",resultado)


#perguntar quantas vezes o usuário quer repetir o número
def repeticao():
    print("-" * 30)

    repeticao = int(input("Quantos números voce quer repetir: "))
    contador = 1
    result = 0
    for number in range(0,repeticao):
        number = float(input(f"Qual o {contador} número? "))
        contador += 1
        result += number
    print("Resultado: ",result)


def calculadora_normal():
    while True:

        valor1 = float(input("Digite o Primeiro Número: "))
        valor2 = float(input("Digite o Segundo Número: "))
        print("-" * 50)
        soma = valor1 + valor2
        print("Soma : ", soma)
        print("-" * 50)
        subtracao = valor1 - valor2
        print("Subtracao : ", subtracao)
        print("-" * 50)
        if valor2 == 0:
            print('O segundo número da Divisão não pode ser 0')
        else:
            divisao = valor1 / valor2
            print("Divisão: ", divisao)
        print("-" * 50)
        multiplicacao = valor1 * valor2
        print("Multiplicação: ", multiplicacao)

        break


while True:
    print("-" * 25)
    print("Calculadora Python! ")

    print("Digite 1 para descobrir a raiz quadrada de um número\n"
          + "Digite 2 para somar 3 números\n"
            + "Digite 3 para inserir a quantidade de números que voce deseja somar\n"
                + "Digite 4 para fazer as 4 operações básicas dos números inseridos\n "
          +"Se deseja sair digite 5:  ")
    print("-" * 20)


    escolha = int(input("Escolha nossos tipos de cálculo de 1 a 5: "))

    if escolha == 5:
        break
    elif escolha == 1:
        raiz_quadrada()

    elif escolha == 2:
        somar3_numeros()

    elif escolha == 3:
        repeticao()

    elif escolha == 4:
        calculadora_normal()
    else:
        print("Valor inserido incorretamente! Tente de novo! ")









