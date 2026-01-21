def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Qual seu peso em (kg): "))
altura = float(input("Qual sua altura em (m): "))

imc = calcular_imc(peso, altura)
print ("Seu IMC é: ", imc)
