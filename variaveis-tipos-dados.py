# Declaração das variáveis
id = ""
nome = ""
salario = 0.0
brasileiro = False

# Entrada de dados do usuário
id = input("Digite seu ID: ")
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
brasileiro = input("Você é brasileiro? (True/False): ") == "True"

# Saída de dados utilizando f-strings
print("\n--- Dados Informados ---")
print(f"ID: {id}")
print(f"Nome: {nome}")
print(f"Salário: R$ {salario:.2f}")
print(f"Brasileiro: {brasileiro}")
