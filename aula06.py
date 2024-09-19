def verificar_férias(tempo_serviço, mês):
   
    temporada_alta = ["junho", "julho", "dezembro"]
    
    if tempo_serviço > 3:
        return "Pedido de férias aprovado!"
    
    elif mês.lower() in temporada_alta:
        return "Pedido de férias negado. Funcionários com menos de 3 anos de serviço não podem tirar férias durante a temporada alta."
    
    else:
        return "Pedido de férias aprovado!"

def main():
    try:
        tempo_serviço = float(input("Digite o tempo de serviço do funcionário (em anos): "))
        mês = input("Digite o mês em que o funcionário deseja tirar férias: ").strip()
        
        resultado = verificar_férias(tempo_serviço, mês)
        
        print(resultado)
    
    except ValueError:
        print("Por favor, insira um número válido para o tempo de serviço.")

if __name__ == "__main__":
    main()