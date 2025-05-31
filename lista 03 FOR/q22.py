def main():
    n = int(input("Quantidade de fichas: "))

    mais_magro = float('inf')
    mais_gordo = float('-inf')
    id_magro = 0
    id_gordo = 0

    for i in range(n):
        numero = int(input('Número de identificação: '))
        peso = int(input('Peso do boi(kg): '))

        if peso < mais_magro:
            mais_magro = peso
            id_magro = numero

        if peso > mais_gordo:
            mais_gordo = peso
            id_gordo = numero

    print(f'Mais magro: ID {id_magro}, peso {mais_magro}kg')
    print(f'Mais gordo: ID {id_gordo}, peso {mais_gordo}kg')

main()