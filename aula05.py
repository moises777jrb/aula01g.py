def soma_impares(X, Y):
    if X > Y:
        X, Y = Y, X
    if X % 2 == 0:
        X += 1
    if Y % 2 == 0:
        Y -= 1
    if X > Y:
        return 0
    n = (Y - X) // 2 + 1
    soma = n * (X + Y) // 2
    
    return soma

def main():
    N = int(input("Escreva a entrada: "))
    
    resultados = []
    for _ in range(N):
        X, Y = map(int, input().split())
        resultado = soma_impares(X, Y)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "_main_":
    main()