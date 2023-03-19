print("Digite 1 para à vista em dinheiro ou cheque")
print("Digite 2 para à vista no cartão de crédito")
print("Digite 3 para parcelar em 2 vezes")
print("Digite 4 para parcelar em 4 vezes")

escolha = int(input("Digite o código escolhido: "))

if (escolha == 1):
    preço = float(input("Digite o valor do produto: "))
    valor1 = preço*0.9
    print("O valor final é de {}, tendo 10% de desconto!".format(valor1))
elif (escolha == 2):
    preço = float(input("Digite o valor do produto: "))
    valor2 = preço*0.95
    print("O valor final é de {}, tendo 5% de desconto!".format(valor2))
elif (escolha == 3):
    preço = float(input("Digite o valor do produto: "))
    print("O pagamento será realizado em duas parcelas de {} reais".format(preço/2))
elif (escolha == 4):
    preço = float(input("Digite o valor do produto: "))
    juros = 0.07
    parcela = preço/4
    pagamento = parcela*(1+juros)
    print("O pagamento será realizado em 4 parcelas de {} reais, com juros de {}%".format(pagamento, juros))
else:
    print("Não foi feita a escolha certa entre os dígitos apresentados!")
