def main():
    n = int(input("Digite o valor de N: "))

    s = 0
    
    for i in range(1, n + 1):
        s += i / (n - i + 1)

    print(f"S = {s:.2f}")

main()