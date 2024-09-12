import os
os.system("cls")

def calcular_media():
    while True:
        nome = input("Informe o nome do aluno ou digite a palavra 'sair' para encerrar: ")
        if nome.lower() == 'sair':
            break
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2
        print(f"A média de {nome} é {media:.2f}")

# Executa o sistema
calcular_media()