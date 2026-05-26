# Solicita o valor em metros
metros = float(input("Digite o valor em metros: "))

# Cálculos de conversão
centimetros = metros * 100
milimetros = metros * 1000

# Exibição dos resultados
print(f"{metros} metros equivalem a {centimetros:.0f} centímetros.")
print(f"{metros} metros equivalem a {milimetros:.0f} milímetros.")
