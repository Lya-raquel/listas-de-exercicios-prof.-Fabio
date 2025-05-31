# 12. Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

def main():
    qtd = int(input('Quantos números quer adicionar na lista? '))

    soma = 0
    for i in range(qtd):
        n = int(input('N: '))
        soma += n
        media = soma / qtd
    print(f'Somatório dos valores: {soma}.')
    print(f'Média: {media:.2f}')

main()