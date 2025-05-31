# 5. Leia um número, calcule e escreva seu fatorial.

def main():
    num = int(input('Valor: '))

    result = 1
    for i in range(num, 1, - 1):  
        result *= i
    print(f'Fatrorial de {num} = {result}')  

main()