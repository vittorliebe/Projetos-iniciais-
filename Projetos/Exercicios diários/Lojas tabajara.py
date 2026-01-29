# sistema de loja de supermercado e dando um troco
valor = 1
total = 0
contador = 1
print("Bem vindo A loja Tabajara ")
print("-"*30)

while valor > 0:
    valor = float(input(f"Produto {contador} R$:"))
    contador += 1
    total += valor
print(f"Total: {total}")
dinheiro = float(input("Qual o valor: "))
troco = dinheiro - total
if troco > dinheiro:
    print("Dinheiro insuficiente")
else:
    print(f'Troco é {troco}')