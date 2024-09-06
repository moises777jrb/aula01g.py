numero = int(input("digite o numero de funcionarios"))
horas_trabalhadas = int(input("digite o numero de horas trabalhadas"))
valor_por_hora = float(input("digite o numero de valor por hora"))

salario = horas_trabalhadas * valor_por_hora

print(f'Número = {numero}')
print(f'Salário = $ {salario:.2f}')