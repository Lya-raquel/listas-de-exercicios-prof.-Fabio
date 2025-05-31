# 11. Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

def main():
    limite_inf = int(input('Limite Inferior: '))
    limite_sup = int(input('Limite Superior: '))

    for num in range(limite_inf, limite_sup + 1):
        if num > 1:
            for i in range (2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(f'{num} é primo.')
        
        
main()      
      
