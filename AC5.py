#1 
def imprimir_padrao_exclusivo(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="   ")
        print(f"... {i}   {n}")

n = int(input("Digite o valor de n: "))
imprimir_padrao_exclusivo(n)

#2
def contar_digitos(numero):
    num_str = str(numero)
    qtd_digitos = len(num_str)
    return qtd_digitos

numero = 12345
quantidade_de_digitos = contar_digitos(numero)
print(f'O número {numero} tem {quantidade_de_digitos} dígitos.')

#3
try:
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite outro número inteiro: "))
    resultado = num1 / num2
except ValueError:
    print("Desculpe, você precisa fornecer números inteiros válidos.")
except ZeroDivisionError:
    print("Desculpe, a divisão por zero não é permitida.")
finally:
    try:
        print("O resultado da operação é:", resultado)
    except NameError:
        print("Ocorreu um erro e não foi possível calcular o resultado.")
