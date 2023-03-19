num = int(input("Digite um número: "))
i = 0
tam = str(num)
soma = 0

while i < len(tam):
    resto = (num//(10**i))%10
    i = i + 1
    soma = soma + resto
print(soma)

