# 9. Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.

def main():
    limite_inf = int(input('Limite Inferior: '))
    limite_sup = int(input('Limite Superior: '))

    print(f'Números pares entre {limite_inf} e {limite_sup}: ', end = ' ')

    for par in range(limite_inf, limite_sup):
        if par % 2 == 0:
            print(par, end = ' ')
            

main()