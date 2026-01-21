def porcentagem(valor1, taxa,):
    return (valor1 * taxa / 100)


valor1 =int(input("Valor 1: "))
taxa = int(input("taxa :"))
result = (valor1 * taxa / 100)
resposta = porcentagem(valor1,taxa)
print('Valor da Taxa é: ',resposta)
print('Somado com a taxa ',valor1, '+',result, "=",valor1 + result)
