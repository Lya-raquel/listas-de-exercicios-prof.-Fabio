# 14. Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
# maior quadrado menor que 38 é 36 (quadrado de 6).


def main():
    n = int(input('N: '))

    for i in range(0, n):
        raiz = int(n ** 0.5)
        maior_quadrado_menor = raiz ** 2
    print(f'Maior quadrado menor que {n} é {maior_quadrado_menor}(quadrado de {raiz})')


main()