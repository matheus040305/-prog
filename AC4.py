#1
def e_primo(num):
    if num <= 1:
        return False 

    for i in range(2, num):
        if num % i == 0:
            
            divisores = [i for i in range(2, num) if num % i == 0]
            return False, divisores

    return True 


numero = 17
resultado, divisores = e_primo(numero)
if resultado:
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo. É divisível por: {divisores}')

    #2
def calcular_juros(valor_divida, parcelas):
    if parcelas == 1:
        return 0
    elif parcelas == 3:
        return valor_divida * 0.10
    elif parcelas == 6:
        return valor_divida * 0.15
    elif parcelas == 9:
        return valor_divida * 0.20
    elif parcelas == 12:
        return valor_divida * 0.25
    else:
        return None

def calcular_total_divida(valor_divida, parcelas):
    juros = calcular_juros(valor_divida, parcelas)
    if juros is not None:
        return valor_divida + juros
    else:
        return None

def imprimir_opcoes(valor_divida):
    print("Quantidade de Parcelas  % de Juros Valor Total     Valor da Parcela")
    for parcelas in [1, 3, 6, 9, 12]:
        juros = calcular_juros(valor_divida, parcelas)
        total_divida = calcular_total_divida(valor_divida, parcelas)
        if juros is not None and total_divida is not None:
            valor_parcela = total_divida / parcelas
            print(f"{parcelas:<22} {juros:<13} R$ {total_divida:<13} {parcelas:<18} R$ {valor_parcela:.2f}")

valor_divida = float(input("Digite o valor da dívida: R$ "))
imprimir_opcoes(valor_divida)

#3
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    numero = int(input("Digite um número positivo (ou um número negativo para sair): "))
    
    if numero < 0:
        break
    
    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1

print("Quantidade de números no intervalo [0-25]:"), interval


