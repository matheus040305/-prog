#1
import random

contagem = [0] * 6

for _ in range(100):
    contagem[random.randint(0, 5)] += 1

print("Resultado dos Lançamentos:")
for valor, frequencia in enumerate(contagem, start=1):
    print(f"Dado {valor}: {frequencia} vezes")

#2
 import json

alunos = {}

print("Cadastro de Alunos")

while True:
    matricula = input("Matrícula (ou 'sair' para encerrar): ")
    if matricula == 'sair':
        break

    nome = input("Nome: ")
    email = input("E-mail: ")

    alunos[matricula] = {'nome': nome, 'e-mail': email}

with open('alunos.json', 'w') as arquivo_json:
    json.dump(alunos, arquivo_json, indent=4)

print("Dados dos alunos foram salvos em 'alunos.json'.")


#3
from datetime import datetime

def data_por_extenso(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return data.strftime('%d de %B de %Y')
    except ValueError:
        return None

def mensagem_personalizada(data_str):
    data_extenso = data_por_extenso(data_str)
    if data_extenso:
        return f"A data {data_str} por extenso: {data_extenso}."
    return f"A data {data_str} é inválida."

data_str = "05/11/2023"
mensagem = mensagem_personalizada(data_str)
print(mensagem)

