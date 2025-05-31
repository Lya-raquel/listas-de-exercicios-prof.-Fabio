# 8. Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

def main():
    n = int(input('N: '))
    limite_inf = int(input('Limite Inferior: '))
    limite_sup = int(input('Limite Superior: '))

    for i in range(limite_inf, limite_sup):
        if i % n == 0:
            print(i)
        i += 1


main()