# 3. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.

def main():
    inicial_a = int(input('Valor iniciao(A0): '))
    limite = int(input('Limite: '))
    razao = int(input('Razão(R): '))

    for num in range(inicial_a, limite, razao):
        print(num)


main()