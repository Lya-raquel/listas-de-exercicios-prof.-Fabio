# 7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

def main():
    n = int(input('N: '))

    soma = 0
    for i in range(1, n + 1 ):
        soma += i
    print(f'Total da soma entre os números de 1 até {n}: {soma} ')


main()