prod = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o valor do desconto: "))

desc = 1 - (desconto/100)
prod_nov = prod*desc

print("O desconto foi de {}% e o novo preço do produto é {}".format(desconto, prod_nov))
