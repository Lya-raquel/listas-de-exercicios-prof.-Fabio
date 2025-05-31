# 2. Leia N e escreva todos os números inteiros pares de 1 a N.

def main():
    n = int(input('N: '))

    for num in range(1, n):
        if num % 2 == 0:
            print(num)

main()