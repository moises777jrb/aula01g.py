def main():
    numeros = []
    print("Digite 10 números:")
    for i in range(10):
        while True:
            try:
                numero = int(input(f"[{i+1}]="))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
    media = sum(numeros) / len(numeros)
    print(f"A média é {media:.1f}")
if __name__ == "__main__":
    main()