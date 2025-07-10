nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

#calcular media
mediafinal = (nota1 + nota2) / 2

#verificação
if mediafinal >= 5.0:
    print("A média: %.1f - Aprovado " % mediafinal)
else:
    print("A média: %.1f - Reprovado "% mediafinal)
