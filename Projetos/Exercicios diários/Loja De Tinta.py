# Faça um programa para uma loja de tintas
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida  em latas de 18 litros, que custam R$ 120,00.Informe
# ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

CONS_PRECO= 120
metro_quadrados = int(input("Quantidade de metros: "))
litro, resto = divmod(metro_quadrados, 3)
if resto > 0:
    litro+= 1
lata,adicional = divmod(litro,18)
if adicional > 0:
    lata += 1
custo = lata * CONS_PRECO
print("Quantidade de latas: ",lata)
print(f"Preço Total R${custo}")

