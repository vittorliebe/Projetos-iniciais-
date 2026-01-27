# Faça um programa que faça 5 perguntas ao usuário sobre um crime.
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima"
# O programa deve no final emitir uma classificão sobre a participação da pessoa no crime.
# Se a pessoa  responder positivamente  a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4  como "Cúmplice" e 5 como "Assasino".Caso contrário, ele será classificado como "Inocente".

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
     "Mora perto da vítima?",
     "Devia para a vítima?",
     "Já trabalhou com a vítima? "
]
analise = 0
for pergunta in perguntas:
    resposta=input(pergunta)
    resposta = 1 if resposta == "s" else 0
    analise += resposta

if analise == 2:
    print('Suspeita')
elif analise > 2 and analise < 5:
    print("Cúmplice")
elif analise == 5:
    print("Assasino")
else:
    print("Inocente")

