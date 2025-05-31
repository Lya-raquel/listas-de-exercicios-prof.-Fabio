# 10. Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.

def main():
    limite_inf = int(input('Limite Inferior: '))
    limite_sup = int(input('Limite Superior: '))

    print(f'Números ímpares entre {limite_inf} e {limite_sup}: ', end = ' ')

    for impar in range(limite_inf, limite_sup):
        if impar % 2 != 0:
            print(impar, end = ' ')
            

main()