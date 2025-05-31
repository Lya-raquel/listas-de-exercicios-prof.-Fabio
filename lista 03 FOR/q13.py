# 13. Leia N e uma lista de N números e escreva o maior número da lista.

def main():
    qtd = int(input('Quantos números quer adicionar na lista? '))

    lista = []
    for i in range(qtd):
        n = int(input('N: '))
        lista.append(n)
        maior = max(lista)
    print(f'Maior número da lista: {maior}')


main()