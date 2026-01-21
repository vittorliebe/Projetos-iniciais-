import os
from datetime import datetime

mensagens = []

nome = input("Digite seu nome: ")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_mensagens():
    for m in mensagens:
        print(f"[{m['hora']}] {m['nome']}: {m['texto']}")


while True:
    limpar_tela()

    mostrar_mensagens()
    print("____________________________")

    texto = input("Mensagem: ")

    if texto == "/sair":
        break

    hora = datetime.now().strftime("%H:%M")

    mensagens.append({
        "nome": nome,
        "texto": texto,
        "hora": hora
    })
