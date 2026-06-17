resultado = []
while True:
    try:
        num = int(input("Digite um número em base decimal: "))
        break
    except ValueError:
        print("Insira um número válido.")
while True:
    try:
        base = int(input(f"Para qual base o {num} será convertido?(Max. 16)"))
        if 2 <= base <= 16:
            break
        else:
            print("Base fora do intervalo permitido.")
    except ValueError:
        print("Insira uma base válida.")
while num > 0:
    if num == 0:
        resultado.append(0)
    elif num % base < 10:
        resultado.append(num % base)
    elif num % base == 10:
        resultado.append("A")
    elif num % base == 11:
        resultado.append("B")
    elif num % base == 12:
        resultado.append("C")
    elif num % base == 13:
        resultado.append("D")
    elif num % base == 14:
        resultado.append("E")
    else:
        resultado.append("F")
    num = num // base

for c in range (len(resultado), 0, -1):
    print(resultado[c - 1], end="")