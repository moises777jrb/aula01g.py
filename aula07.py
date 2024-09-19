def alocar_recursos(nivel_experiencia, tipo_apresentacao):
    # Definições de recursos baseadas no nível de experiência
    recursos = {
        "novato": {
            "workshop": {"tempo": "30 minutos", "equipamento": "básico", "sala": "pequena"},
            "palestra": {"tempo": "20 minutos", "equipamento": "básico", "sala": "pequena"},
            "demonstração": {"tempo": "25 minutos", "equipamento": "básico", "sala": "pequena"}
        },
        "experiente": {
            "workshop": {"tempo": "45 minutos", "equipamento": "intermediário", "sala": "média"},
            "palestra": {"tempo": "30 minutos", "equipamento": "intermediário", "sala": "média"},
            "demonstração": {"tempo": "35 minutos", "equipamento": "intermediário", "sala": "média"}
        },
        "especialista": {
            "workshop": {"tempo": "60 minutos", "equipamento": "avançado", "sala": "grande"},
            "palestra": {"tempo": "45 minutos", "equipamento": "avançado", "sala": "grande"},
            "demonstração": {"tempo": "50 minutos", "equipamento": "avançado", "sala": "grande"}
        }
    }
  
    if nivel_experiencia in recursos and tipo_apresentacao in recursos[nivel_experiencia]:
        return recursos[nivel_experiencia][tipo_apresentacao]
    else:
        return {"tempo": "não definido", "equipamento": "não definido", "sala": "não definida"}

def main():
    try:
        
        nivel_experiencia = input("Digite o nível de experiência do palestrante (novato, experiente, especialista): ").strip().lower()
        tipo_apresentacao = input("Digite o tipo de apresentação (workshop, palestra, demonstração): ").strip().lower()

        recursos = alocar_recursos(nivel_experiencia, tipo_apresentacao)
        
        print("\nRecursos alocados para a apresentação:")
        print(f"Tempo de apresentação: {recursos['tempo']}")
        print(f"Tipo de equipamento: {recursos['equipamento']}")
        print(f"Tipo de sala: {recursos['sala']}")
    
    except Exception as e:
        print(f"Erro: {e}. Por favor, insira dados válidos.")

if __name__ == "__main__":
    main()