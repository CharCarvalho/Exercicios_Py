seq = int(input("Digite o tamanho da sequencia: "))
i = 0
soma = 0

while (seq > i):
    i = i + 1
    if (i % 2 == 0):
        soma = soma + i
print(soma)