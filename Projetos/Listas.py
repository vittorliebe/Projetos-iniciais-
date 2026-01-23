# Lista é uma colecao ordenada e mutável. Permite membros duplicados.
#Index:     0     1    2  3
lista = ["Carro",True,5.5,2]
print(lista)
print(type(lista))
print(lista[2])
print("-"*30)
# Tuplas é uma colecao ordenada e imutável. Permite membros duplicados.
tupla = ("Carro", True,2,5.5)
print (tupla)
print(type(tupla))
print(tupla[1])
print("-"*30)
# O dicionario é uma colecao ordenada e mutável. Nenhum membro duplicado.
              #chave   valor
dicionario = {"nome": "Carro","Logico": True,"Numerico": 2,"Outro Numero": 5.5 }
print(dicionario)
print(type(dicionario))
print(dicionario["nome"])
print("-"*30)

# Set é uma colecao não ordenada e não indexada. Nenhum membro duplicado.
conjunto ={"Carro", True, 2, 5.5}
print(conjunto)
print(type(conjunto))