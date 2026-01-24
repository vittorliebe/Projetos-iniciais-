def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        numero -=1



print("-"*30)
#Outro Jeito de Fazer
def contagem_regressiva2(numero):
    while True:
        print(numero)
        numero -=1
        if numero <= 0:
            break


#Outro jeito de Fazer
def contagem_regressiva3(numero):
    for i in range(numero,-1,-1):
        print(i)



#Proximo exercício: Maior Numero de uma lista
def maior_numero (lista_numero):
    maior_numero = lista_numero[0]
    for numero in lista_numero:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

lista = [4,6,7,10,2,15]
maior_numero_lista = maior_numero(lista)
print(f"O maior número da lista é {maior_numero_lista}")

#Outro Jeito de fazer
def maior_numero2 (lista_numero):
    # a palavra max pega o numero maior automaticamente de uma lista
    maior_numero = max(lista_numero)
    return maior_numero
lista = [10,5,10,57,1000]
maior_numerolista = maior_numero2(lista)
print(f"O maior número da lista é {maior_numerolista}")

#    Max é para achar o Maior
#    Min é para achar o Menor
#    Len é para contar o numero de indexadores
