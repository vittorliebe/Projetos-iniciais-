#raiz quadrada, 1 aplicação da lib math
import math
print("-"*30)
print("A calculadora python! ")
print("-"*30)

numero = float(input(f"O número para a raiz quadrada: \n"))
raiz = math.sqrt(numero)
print("Resultado: " + str(raiz))


#somar 3 números
resultado = 0
contador = 1
for entrada in range(1,4):
    entrada = int(input(f"O {contador} número é: "))
    resultado += entrada
    contador += 1
print("O resultado é: ",resultado)


