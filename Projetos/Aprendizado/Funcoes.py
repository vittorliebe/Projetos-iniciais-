def minha_funcao():
    name = "Vittor"
    print(f"Essa é minha funcao! Prazer, {name}!")
minha_funcao()


def somar(n1, n2):
    resultado = n1 + n2
    return  resultado
resultado_soma = somar(10,10)
print(resultado_soma)



def saudacao(nome):
    print(f"Prazer {nome}")
saudacao("Vittor")

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
if verificar_par(5):
    print("É par")
else:
    print("É impar")

#Colocar 1 * no parametro da funcao faz ele conseguir entregar varios numeros, virou uma tupla
def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado
soma_da_lista = somar_lista(4,5,6,78,2,7,3,67,13,)
print(f"O resultado da Soma é {soma_da_lista}")


def calculo_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / qtd
    return media
resultado = calculo_media(6,8,3,5,9,)
print(f"A média é {resultado} ")

#Colocar 2 * vai fazer com que o parametro entregue um dicionario
def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

informacoes_pessoais(nome= "Vittor", idade= 20, jogo_preferido = "Lol", time= "Reset")




