num = int(input("Digite um numero: "))
tam = str(num)
soma = 0
i = 0
while i < len(tam):
    resto = (num//10**i)%10
    soma = soma + resto
    i = i + 1
print(soma)