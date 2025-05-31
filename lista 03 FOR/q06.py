# 6. Escreva a tabuada dos números de 1 a 10.

def main():
    result = 1
    contador = 1
    for i in range(1, 11):
        total = result * contador
        print(f'{i} x {contador} = {total}')
        contador += 1
        result += 1
        

main()