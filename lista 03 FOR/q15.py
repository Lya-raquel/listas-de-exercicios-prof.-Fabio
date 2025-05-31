# 15. Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

def main():
    n = int(input('N: '))

    for n in range(1, n + 1):
        termo = (n * (n + 1)) // 2
        print(termo, end=' ')



main()