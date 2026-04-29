resultado = []
while True:
    try:
        num = int(input("Digite um número em base decimal: "))
        break
    except ValueError:
        print("Insira um número válido.")
while True:
    try:
        base = int(input(f"Para qual base o {num} será convertido? "))
        break
    except:
        print("Base não identificada")
while num > 0:
    resultado.append(num % base)
    num = num // base

for c in range (len(resultado), 0, -1):
    print(resultado[c - 1], end="")
